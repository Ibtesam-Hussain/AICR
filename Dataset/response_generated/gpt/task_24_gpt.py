# Task: Write a function that converts a price string like "$1,234.56" into a float.

def parse_price(price_str):
    return float(price_str.replace('$', '').replace(',', ''))
