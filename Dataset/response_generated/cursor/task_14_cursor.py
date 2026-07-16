from urllib.parse import urlencode


def build_query_string(filters: dict) -> str:
    params = {}
    for key, value in filters.items():
        if value is None or value == "":
            continue
        if isinstance(value, (list, tuple)) and not value:
            continue
        params[key] = value
    return urlencode(params, doseq=True)