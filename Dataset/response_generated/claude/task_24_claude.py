# Task: Write a function that converts a price string like "$1,234.56" into a float.

def parse_price(price_string: str) -> float:
    """Convert a price string like '$1,234.56' to a float."""
    return float(price_string.replace('$', '').replace(',', ''))
