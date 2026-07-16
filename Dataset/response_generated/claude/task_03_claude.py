# Task: Write a function to merge two dictionaries, combining values for keys that exist in both.

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dictionaries, combining values for duplicate keys.
    Values are combined into lists.
    """
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    
    return result

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dictionaries, combining values for duplicate keys into lists.
    """
    result = {**dict1}
    
    for key, value in dict2.items():
        result[key] = [result[key], value] if key in result else value
    
    return result

from collections import defaultdict

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dictionaries, combining duplicate key values into lists.
    """
    result = defaultdict(list)
    
    for d in [dict1, dict2]:
        for key, value in d.items():
            result[key].append(value)
    
    return dict(result)
