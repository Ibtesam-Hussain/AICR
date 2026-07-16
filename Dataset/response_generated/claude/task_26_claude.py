# Task: Write a function that rounds a number to 2 decimal places for currency display.

def format_currency(amount: float) -> float:
    """Rounds a number to 2 decimal places for currency display."""
    return round(amount, 2)

def format_currency(amount: float) -> str:
    """Returns a currency-formatted string rounded to 2 decimal places."""
    return f"{amount:.2f}"
