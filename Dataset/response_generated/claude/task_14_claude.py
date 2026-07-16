from urllib.parse import urlencode

def build_query_string(params: dict) -> str:
    """
    Build a URL query string from a dictionary of filter parameters.
    Skips keys with None values. Lists become repeated keys.
    """
    filtered = {k: v for k, v in params.items() if v is not None}
    return urlencode(filtered, doseq=True)