import secrets

def generate_reset_token(length: int = 32) -> str:
    return secrets.token_urlsafe(length)