import re

PHONE_PATTERN = re.compile(
    r"^(?:\+1[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$"
)


def is_valid_phone_number(phone: str) -> bool:
    return bool(PHONE_PATTERN.match(phone.strip()))
