def merge_dicts(left: dict, right: dict, *, combine=None) -> dict:
    result = left.copy()
    for key, value in right.items():
        if key not in result:
            result[key] = value
        elif combine is not None:
            result[key] = combine(result[key], value)
        elif isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value, combine=combine)
        elif isinstance(result[key], list) and isinstance(value, list):
            result[key] = result[key] + value
        else:
            result[key] = value
    return result