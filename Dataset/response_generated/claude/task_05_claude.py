def flatten_json(obj, parent_key='', sep='.'):
    """
    Flatten a nested JSON-like object (dicts and lists) into a
    single-level dictionary with dot-notation (and bracket-index) keys.

    Example:
        {"a": {"b": 1, "c": [2, 3]}} -> {"a.b": 1, "a.c[0]": 2, "a.c[1]": 3}
    """
    items = {}

    if isinstance(obj, dict):
        for key, value in obj.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
            items.update(flatten_json(value, new_key, sep=sep))
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            new_key = f"{parent_key}[{i}]"
            items.update(flatten_json(value, new_key, sep=sep))
    else:
        items[parent_key] = obj

    return items