import secrets

def generate_password_reset_token(length: int = 32) -> str:
    """
    Generate a cryptographically secure URL-safe token for password reset links.

    Args:
        length: Approximate number of random bytes to use. The resulting string
                will be URL-safe and around 1.3x this length in characters.

    Returns:
        A secure, URL-safe token.
    """
    return secrets.token_urlsafe(length)