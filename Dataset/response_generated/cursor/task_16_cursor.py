import copy
import re
from typing import Any

SENSITIVE_KEYS = {
    "password", "passwd", "secret", "token", "access_token", "refresh_token",
    "api_key", "apikey", "authorization", "auth", "cvv", "cvc", "pin",
    "ssn", "social_security", "credit_card", "creditcard", "card_number",
    "cardnumber", "account_number", "accountnumber", "routing_number",
}

CARD_PATTERN = re.compile(r"\b(?:\d[ -]?){13,19}\b")
SSN_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")

MASK = "***REDACTED***"


def _mask_card(value: str) -> str:
    digits = re.sub(r"\D", "", value)
    if len(digits) < 4:
        return MASK
    return f"**** **** **** {digits[-4:]}"


def _mask_value(key: str, value: Any) -> Any:
    if value is None:
        return None

    key_lower = key.lower()

    if key_lower in SENSITIVE_KEYS or any(part in key_lower for part in ("password", "secret", "token", "cvv", "cvc", "ssn", "card", "account")):
        if isinstance(value, str):
            if "card" in key_lower or CARD_PATTERN.search(value):
                return _mask_card(value)
            if "ssn" in key_lower or SSN_PATTERN.search(value):
                return "***-**-****"
            return MASK
        return MASK

    if isinstance(value, str):
        masked = CARD_PATTERN.sub(lambda m: _mask_card(m.group(0)), value)
        masked = SSN_PATTERN.sub("***-**-****", masked)
        return masked

    return value


def mask_sensitive_fields(data: dict[str, Any]) -> dict[str, Any]:
    """Return a deep copy of data with sensitive fields masked for logging."""
    masked = copy.deepcopy(data)

    def _walk(obj: Any) -> Any:
        if isinstance(obj, dict):
            return {k: _walk(_mask_value(k, v)) if not isinstance(v, (dict, list)) else _walk(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_walk(item) for item in obj]
        return obj

    return _walk(masked)