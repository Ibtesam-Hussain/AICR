from collections.abc import Mapping


def merge_dicts(dict1: Mapping, dict2: Mapping) -> dict:
    """
    Merge two dictionaries.

    - Keys present in only one dictionary are copied as-is.
    - For keys present in both, their values are combined:
      - If both values are lists, they are concatenated.
      - Otherwise, the values are placed into a list.
    """
    result = dict(dict1)

    for key, value in dict2.items():
        if key not in result:
            result[key] = value
        else:
            existing = result[key]
            if isinstance(existing, list) and isinstance(value, list):
                result[key] = existing + value
            elif isinstance(existing, list):
                result[key] = existing + [value]
            elif isinstance(value, list):
                result[key] = [existing] + value
            else:
                result[key] = [existing, value]

    return result