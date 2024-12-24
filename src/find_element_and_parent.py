from typing import TypedDict
from xmlschema.validators.elements import XsdElement


class ElementAndParentDict(TypedDict):
    element: XsdElement
    parent: XsdElement
    level: int


def find_element_and_parent(xsd_element, element_dict) -> ElementAndParentDict:
    hierarchy = _get_hierarchy(element_dict)

    if hierarchy[-1] != xsd_element.name:
        raise ValueError(
            "The root element in the dictionary does not match the XsdElement root.")

    current_xsd_element = xsd_element
    parent_xsd_element = xsd_element

    for elem_name in reversed(hierarchy):
        if xsd_element.name == elem_name:
            continue

        parent_xsd_element = current_xsd_element
        current_xsd_element = current_xsd_element.find(elem_name)

        if current_xsd_element is None:
            return None

    return {"element": current_xsd_element, "parent": parent_xsd_element, "level": len(hierarchy) - 1}


def _get_hierarchy(element_dict):

    hierarchy = []

    current_elem = element_dict

    while current_elem:
        hierarchy.append(current_elem['elem_name'])
        current_elem = current_elem.get('parent')

    return hierarchy
