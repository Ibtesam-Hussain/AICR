import re

def validate_registration(payload: dict) -> tuple[bool, list[str]]:
    """
    Validates a user registration payload.

    Args:
        payload: dict expected to contain 'email', 'password', 'age'

    Returns:
        (is_valid, errors) where errors is a list of error messages
    """
    errors = []

    email = payload.get("email")
    password = payload.get("password")
    age = payload.get("age")

    # Email validation
    if not email or not isinstance(email, str):
        errors.append("Email is required and must be a string.")
    else:
        email = email.strip()
        email_regex = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(email_regex, email):
            errors.append("Email format is invalid.")
        elif len(email) > 254:
            errors.append("Email is too long.")

    # Password validation
    if not password or not isinstance(password, str):
        errors.append("Password is required and must be a string.")
    else:
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if len(password) > 128:
            errors.append("Password is too long.")
        if not re.search(r"[A-Z]", password):
            errors.append("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            errors.append("Password must contain at least one lowercase letter.")
        if not re.search(r"\d", password):
            errors.append("Password must contain at least one digit.")
        if not re.search(r"[^\w\s]", password):
            errors.append("Password must contain at least one special character.")

    # Age validation
    if age is None:
        errors.append("Age is required.")
    else:
        try:
            age_int = int(age)
            if isinstance(age, bool):
                raise ValueError
            if age_int < 13:
                errors.append("User must be at least 13 years old.")
            elif age_int > 120:
                errors.append("Age is not valid.")
        except (ValueError, TypeError):
            errors.append("Age must be a valid integer.")

    return (len(errors) == 0, errors)