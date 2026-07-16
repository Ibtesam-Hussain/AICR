import re


def validate_registration_payload(payload: dict) -> tuple[bool, list[str]]:
    """
    Validates a user registration payload.

    Expected payload:
    {
        "email": str,
        "password": str,
        "age": int
    }

    Returns:
        (is_valid, errors)
    """
    errors = []

    email = payload.get("email")
    password = payload.get("password")
    age = payload.get("age")

    # Email validation
    if not isinstance(email, str) or not email.strip():
        errors.append("Email is required.")
    elif not re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
        errors.append("Invalid email address.")

    # Password validation
    if not isinstance(password, str):
        errors.append("Password is required.")
    else:
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password):
            errors.append("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            errors.append("Password must contain at least one lowercase letter.")
        if not re.search(r"\d", password):
            errors.append("Password must contain at least one digit.")

    # Age validation
    if not isinstance(age, int):
        errors.append("Age must be an integer.")
    elif age < 13:
        errors.append("User must be at least 13 years old.")

    return len(errors) == 0, errors