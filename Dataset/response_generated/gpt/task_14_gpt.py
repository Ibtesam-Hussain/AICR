from urllib.parse import urlencode


def build_query_string(params: dict) -> str:
    """
    Build a URL query string from a dictionary of parameters.

    - Ignores keys with a value of None.
    - Supports list/tuple values by repeating the key.
    """
    filtered = {
        key: value
        for key, value in params.items()
        if value is not None
    }
    return urlencode(filtered, doseq=True)