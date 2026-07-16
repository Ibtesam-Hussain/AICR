from copy import deepcopy

def mask_sensitive_fields(data, sensitive_keys=None, mask="****"):
    """
    Return a copy of the dictionary with sensitive fields masked.

    Args:
        data (dict): Response dictionary.
        sensitive_keys (iterable[str], optional): Keys to mask.
        mask (str): Replacement value for sensitive fields.

    Returns:
        dict: Masked copy of the input dictionary.
    """
    if sensitive_keys is None:
        sensitive_keys = {
            "credit_card",
            "card_number",
            "cc_number",
            "cvv",
            "cvc",
            "password",
            "token",
            "access_token",
            "refresh_token",
            "api_key",
            "secret",
        }

    def _mask(value):
        if isinstance(value, dict):
            return {
                k: (mask if k.lower() in sensitive_keys else _mask(v))
                for k, v in value.items()
            }
        if isinstance(value, list):
            return [_mask(item) for item in value]
        return value

    return _mask(deepcopy(data))