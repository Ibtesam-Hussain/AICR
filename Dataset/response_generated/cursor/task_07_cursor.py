def deduplicate_by_id(items: list[dict]) -> list[dict]:
    seen: set = set()
    result: list[dict] = []

    for item in items:
        item_id = item["id"]
        if item_id in seen:
            continue
        seen.add(item_id)
        result.append(item)

    return result