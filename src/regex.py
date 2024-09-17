import re
from .constants import entity_unit_map, unit_mapping, dimension_patterns

def fallback_search_for_entity_units(extracted_text, entity_name):
    relevant_units = entity_unit_map.get(entity_name, set())
    pattern = rf'(\d+\.?\d*)\s*({"|".join(relevant_units)})'
    match = re.search(pattern, extracted_text, re.IGNORECASE)
    if match:
        value, unit = match.groups()
        standardized_unit = unit_mapping.get(unit.lower(), unit.lower())
        return f"{value} {standardized_unit}"
    return None

def filter_relevant_info(entity_name, extracted_text):
    if entity_name in dimension_patterns:
        pattern = dimension_patterns[entity_name]
        match = re.search(pattern, extracted_text, re.IGNORECASE)
        if match:
            value, unit = match.groups()
            standardized_unit = unit_mapping.get(unit.lower(), unit.lower())
            return f"{value} {standardized_unit}"

    fallback_value = fallback_search_for_entity_units(extracted_text, entity_name)
    if fallback_value:
        return fallback_value

    return ''