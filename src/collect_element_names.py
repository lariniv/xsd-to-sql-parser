def collect_element_names(data, parent=None, results=None) -> list[dict]:
    if results is None:
        results = []

    current_element = None

    if isinstance(data, dict):
        if "@name" in data and "@nillable" in data:
            current_element = {
                "elem_name": data["@name"],
                "parent": parent,
            }
            results.append(current_element)
        else:
            current_element = parent

        for value in data.values():
            if isinstance(value, (dict, list)):
                collect_element_names(
                    value, parent=current_element, results=results)

    elif isinstance(data, list):
        for item in data:
            collect_element_names(item, parent=parent, results=results)

    return results
