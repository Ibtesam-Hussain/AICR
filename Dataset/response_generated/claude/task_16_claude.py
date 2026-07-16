import re

def mask_sensitive_fields(data, sensitive_keys=None, mask_char="*", visible_chars=4):
    """
    Recursively mask sensitive fields in a dict (or list of dicts) before logging.
    Returns a new object; does not mutate the original.
    """
    if sensitive_keys is None:
        sensitive_keys = {
            "card_number", "credit_card", "cc_number", "cvv", "cvc",
            "password", "ssn", "ssn_number", "pin", "account_number",
            "iban", "api_key", "secret", "token", "authorization"
        }
    sensitive_keys = {k.lower() for k in sensitive_keys}

    def mask_value(value):
        if value is None:
            return value
        s = str(value)
        if len(s) <= visible_chars:
            return mask_char * len(s)
        return mask_char * (len(s) - visible_chars) + s[-visible_chars:]

    def is_sensitive_key(key):
        key_lower = str(key).lower()
        return any(sk in key_lower for sk in sensitive_keys)

    def process(obj):
        if isinstance(obj, dict):
            result = {}
            for k, v in obj.items():
                if is_sensitive_key(k):
                    if isinstance(v, (dict, list)):
                        result[k] = process(v)
                    else:
                        result[k] = mask_value(v)
                else:
                    result[k] = process(v)
            return result
        elif isinstance(obj, list):
            return [process(item) for item in obj]
        else:
            return obj

    return process(data)