from collections.abc import Mapping


def flatten_json(data, parent_key="", sep="."):
    """
    Flatten a nested JSON-like dictionary into a flat dictionary
    using dot-notation keys.

    Example:
        {"a": {"b": 1}, "c": 2}
        -> {"a.b": 1, "c": 2}
    """
    flat = {}

    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)

        if isinstance(value, Mapping):
            flat.update(flatten_json(value, new_key, sep))
        else:
            flat[new_key] = value

    return flat