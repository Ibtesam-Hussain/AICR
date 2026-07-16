from collections import defaultdict

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merge two dictionaries, combining values for keys that exist in both."""
    result = dict(dict1)
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], (int, float)) and isinstance(value, (int, float)):
                result[key] = result[key] + value
            elif isinstance(result[key], list) and isinstance(value, list):
                result[key] = result[key] + value
            elif isinstance(result[key], str) and isinstance(value, str):
                result[key] = result[key] + value
            elif isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    return result