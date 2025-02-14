import xmlschema
from collect_element_names import collect_element_names
from find_element_and_parent import find_element_and_parent
from generate_sql import generate_sql
from consts import id_param, src_db_owner, src_db_table, a010, start_date, nn_in_base_detail, path, output_file, table_name

xml_scheme = xmlschema.XMLSchema(path)

root_element = None

xml_dict = xml_scheme.to_dict(path)

element_names = collect_element_names(xml_dict)

nn_in_level = 1

annotation = xml_scheme.annotations

try:
    if a010 is None:
        a010 = annotation[0].documentation[0].text
except:
    print('No annotation found')

try:
    if start_date is None:
        start_date = annotation[0].appinfo[0].text.split(': ')[1]
except:
    print('No start date found')

results = []
after_data_element_found = False

for value in element_names:
    element = None
    parent = None
    level = 1

    if value["parent"] is None:
        element = xml_scheme.elements[value["elem_name"]]
        root_element = xml_scheme.elements[value["elem_name"]]
    else:
        element, parent, level = find_element_and_parent(
            root_element, value).values()

    if after_data_element_found == False:
        if element.name == 'DATA':
            after_data_element_found = True

    element_data_type = ''
    data_scale = None
    data_precision = None
    literal = None
    nillable = 1 if element.nillable else 0

    if element.type.name:
        xsd_type = xml_scheme.types.get(element.type.name)
        if xsd_type is not None:
            if xsd_type.annotation:
                literal = xsd_type.annotation

            if xsd_type.is_decimal():
                element_data_type = "NUMBER"
                for key, value in xsd_type.facets.items():
                    if 'fractionDigits' in key:
                        data_scale = value.value
            elif 'integer' in xsd_type.base_type.name:
                element_data_type = "NUMBER"
            elif xsd_type.is_datetime():
                element_data_type = "DATE"

            elif 'string' in xsd_type.base_type.name:
                element_data_type = "VARCHAR2"

                if xsd_type.max_length:
                    data_precision = xsd_type.max_length

                if isinstance(xsd_type.enumeration, list):
                    is_numeric = all(item.isdigit()
                                     for item in xsd_type.enumeration)
                    is_same_length = all(
                        len(item) == len(xsd_type.enumeration[0]) for item in xsd_type.enumeration)
                    element_data_type = "NUMBER" if is_numeric else "VARCHAR2"
                    data_precision = len(
                        xsd_type.enumeration[0]) if is_same_length else None

                if xsd_type.patterns:
                    regexps = xsd_type.patterns.regexps

                    if isinstance(regexps, list) and len(regexps) == 1:
                        if r'(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.\d\d\d\d' in regexps[0]:
                            element_data_type = "DATE"
                        else:
                            element_data_type = "VARCHAR2"
                            print(
                                f'Manual intervention required in {element.name} to determine the data type\n')
                    else:
                        element_data_type = "VARCHAR2"
                        print(
                            f"More than one regular expression pattern found in {element.name}\n")
    else:
        print(f'No type found for {element.name}\n')
        element_data_type = "VARCHAR2"

    if element_data_type == 'NUMBER' and data_precision is None:
        data_precision = 22

    if element.annotation:
        try:
            literal = element.annotation.documentation[0].text
        except:
            literal = None

    if after_data_element_found:
        parent_id = None

        if parent:
            for value in results:
                if value['tag'] == parent.name:
                    parent_id = value['id']
                    break

        results.append({'id': nn_in_level + id_param,
                        'a010': a010,
                        'lvl': level,
                        'tag': element.name,
                        'id_tag_parent': parent_id,
                        'nn_in_level': nn_in_level,
                        'src_db_owner': src_db_owner,
                        'src_db_table': src_db_table,
                        'src_db_column': element.name,
                        'data_type': element_data_type,
                        'literal': literal,
                        'data_precision': data_precision,
                        'data_scale': data_scale,
                        'nn_in_base_detail': nn_in_base_detail,
                        'f_nil': nillable,
                        'd_open': start_date,
                        'd_close': None
                        })
        nn_in_level += 1


insert_statements = generate_sql(
    results, table_name, output_file)
