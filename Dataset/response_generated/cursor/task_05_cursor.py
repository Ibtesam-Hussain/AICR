def flatten_dict(obj, parent_key="", sep="."):
    flat = {}

    if isinstance(obj, dict):
        if not obj:
            if parent_key:
                flat[parent_key] = obj
            return flat
        for key, value in obj.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
            flat.update(flatten_dict(value, new_key, sep=sep))
    elif isinstance(obj, list):
        if not obj:
            if parent_key:
                flat[parent_key] = obj
            return flat
        for index, value in enumerate(obj):
            new_key = f"{parent_key}{sep}{index}" if parent_key else str(index)
            flat.update(flatten_dict(value, new_key, sep=sep))
    elif parent_key:
        flat[parent_key] = obj

    return flat