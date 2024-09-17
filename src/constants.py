# Define the unit mappings and entity unit map
entity_unit_map = {
    'width': {'centimetre', 'cm', 'foot', 'ft', 'inch', 'in', '"', 'metre', 'm', 'millimetre', 'mm', 'yard', 'yd'},
    'depth': {'centimetre', 'cm', 'foot', 'ft', 'inch', 'in', '"', 'metre', 'm', 'millimetre', 'mm', 'yard', 'yd'},
    'height': {'centimetre', 'cm', 'foot', 'ft', 'inch', 'in', '"', 'metre', 'm', 'millimetre', 'mm', 'yard', 'yd'},
    'item_weight': {'gram', 'g', 'kilogram', 'kg', 'microgram', 'μg', 'milligram', 'mg', 'ounce', 'oz', 'pound', 'lb', 'ton'},
    'maximum_weight_recommendation': {'gram', 'g', 'kilogram', 'kg', 'microgram', 'μg', 'milligram', 'mg', 'ounce', 'oz', 'pound', 'lb', 'ton'},
    'voltage': {'kilovolt', 'kv', 'millivolt', 'mv', 'volt', 'v'},
    'wattage': {'kilowatt', 'kw', 'watt', 'w'},
    'item_volume': {'centilitre', 'cl', 'cubic foot', 'ft³', 'cubic inch', 'in³', 'cup', 'decilitre', 'dl', 'fluid ounce', 'fl oz', 'gallon', 'gal', 'imperial gallon', 'litre', 'l', 'microlitre', 'µl', 'millilitre', 'ml', 'pint', 'quart'}
}

unit_mapping = {
    'cm': 'centimetre',
    'ft': 'foot',
    'in': 'inch',
    '"': 'inch',
    'm': 'metre',
    'mm': 'millimetre',
    'yd': 'yard',
    'g': 'gram',
    'kg': 'kilogram',
    'μg': 'microgram',
    'mg': 'milligram',
    'oz': 'ounce',
    'lb': 'pound',
    'ton': 'ton',
    'kv': 'kilovolt',
    'mv': 'millivolt',
    'v': 'volt',
    'kw': 'kilowatt',
    'w': 'watt',
    'cl': 'centilitre',
    'ft³': 'cubic foot',
    'in³': 'cubic inch',
    'dl': 'decilitre',
    'fl oz': 'fluid ounce',
    'gal': 'gallon',
    'l': 'litre',
    'µl': 'microlitre',
    'ml': 'millilitre',
    'pint': 'pint',
    'quart': 'quart'
}

# Dimension-specific regex patterns
dimension_patterns = {
    'width': r'(\d+\.?\d*)\s*(cm|mm|inch|in|ft|m)',
    'depth': r'(\d+\.?\d*)\s*(cm|mm|inch|in|ft|m)',
    'height': r'(\d+\.?\d*)\s*(cm|mm|inch|in|ft|m)'
}