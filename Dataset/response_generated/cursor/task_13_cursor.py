import base64
import json
import time


def is_jwt_expired(token: str, *, leeway: int = 0) -> bool:
    """Return True if the token is expired, invalid, or has no exp claim."""
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return True

        payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
        payload = json.loads(base64.urlsafe_b64decode(payload_b64))

        exp = payload.get("exp")
        if not isinstance(exp, (int, float)):
            return True

        return time.time() >= (exp - leeway)
    except (ValueError, json.JSONDecodeError, TypeError):
        return True