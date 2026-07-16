def dedupe_by_id(items):
    seen = set()
    result = []
    for item in items:
        item_id = item.get("id")
        if item_id not in seen:
            seen.add(item_id)
            result.append(item)
    return result