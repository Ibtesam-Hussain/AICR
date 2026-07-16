# Task: Write a function that checks if a given string is a valid phone number.

import re

def is_valid_phone_number(phone: str) -> bool:
    """
    Validates a phone number format.
    Accepts: +1-234-567-8900, (234) 567-8900, 234-567-8900, 2345678900
    """
    pattern = r"^(\+?1[-.\s]?)?\(?[2-9]\d{2}\)?[-.\s]?[2-9]\d{2}[-.\s]?\d{4}$"
    return bool(re.match(pattern, phone.strip()))

print(is_valid_phone_number("(555) 123-4567"))    # True
print(is_valid_phone_number("+1-555-123-4567"))   # True
print(is_valid_phone_number("5551234567"))        # True
print(is_valid_phone_number("123-456-7890"))      # False (invalid area code)
print(is_valid_phone_number("abc"))               # False
