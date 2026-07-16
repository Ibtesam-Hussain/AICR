def deduplicate_by_id(items):
    """
    Deduplicate a list of dictionaries based on the "id" field.
    Keeps the first occurrence of each unique id.
    """
    seen = set()
    result = []

    for item in items:
        item_id = item.get("id")
        if item_id not in seen:
            seen.add(item_id)
            result.append(item)

    return result