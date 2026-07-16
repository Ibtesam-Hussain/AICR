import re
from typing import Any

EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)
MIN_PASSWORD_LENGTH = 8
MIN_AGE = 13
MAX_AGE = 150


def validate_registration(payload: dict[str, Any]) -> tuple[bool, dict[str, list[str]]]:
    errors: dict[str, list[str]] = {}

    email = payload.get("email")
    if not isinstance(email, str) or not email.strip():
        errors.setdefault("email", []).append("Email is required.")
    elif not EMAIL_PATTERN.match(email.strip()):
        errors.setdefault("email", []).append("Email is invalid.")

    password = payload.get("password")
    if not isinstance(password, str) or not password:
        errors.setdefault("password", []).append("Password is required.")
    else:
        if len(password) < MIN_PASSWORD_LENGTH:
            errors.setdefault("password", []).append(
                f"Password must be at least {MIN_PASSWORD_LENGTH} characters."
            )
        if not re.search(r"[A-Z]", password):
            errors.setdefault("password", []).append(
                "Password must contain at least one uppercase letter."
            )
        if not re.search(r"[a-z]", password):
            errors.setdefault("password", []).append(
                "Password must contain at least one lowercase letter."
            )
        if not re.search(r"\d", password):
            errors.setdefault("password", []).append(
                "Password must contain at least one digit."
            )

    age = payload.get("age")
    if age is None or age == "":
        errors.setdefault("age", []).append("Age is required.")
    elif not isinstance(age, int) or isinstance(age, bool):
        errors.setdefault("age", []).append("Age must be an integer.")
    elif not MIN_AGE <= age <= MAX_AGE:
        errors.setdefault("age", []).append(
            f"Age must be between {MIN_AGE} and {MAX_AGE}."
        )

    return len(errors) == 0, errors