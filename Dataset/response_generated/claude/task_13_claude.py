import time
import base64
import json
import binascii


def is_jwt_expired(token: str) -> bool:
    """
    Check if a JWT-style token has expired based on its 'exp' claim.

    Returns True if the token is expired, malformed, or missing an 'exp' claim.
    Returns False only if the token is well-formed and not yet expired.
    """
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return True

        payload_b64 = parts[1]
        # Add padding back for base64url decoding
        padding = "=" * (-len(payload_b64) % 4)
        payload_bytes = base64.urlsafe_b64decode(payload_b64 + padding)
        payload = json.loads(payload_bytes)

        exp = payload.get("exp")
        if exp is None:
            return True

        return time.time() >= float(exp)

    except (ValueError, TypeError, binascii.Error, json.JSONDecodeError):
        return True