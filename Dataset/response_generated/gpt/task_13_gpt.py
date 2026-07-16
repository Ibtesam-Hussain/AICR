import base64
import json
import time


def is_jwt_expired(token: str, leeway: int = 0) -> bool:
    """
    Returns True if the JWT has expired, False otherwise.

    Args:
        token: JWT string in the format header.payload.signature
        leeway: Optional number of seconds to tolerate clock skew.

    Raises:
        ValueError: If the token format or payload is invalid.
    """
    try:
        _, payload_b64, _ = token.split(".")
    except ValueError as exc:
        raise ValueError("Invalid JWT format") from exc

    # Add required Base64 padding
    payload_b64 += "=" * (-len(payload_b64) % 4)

    try:
        payload = json.loads(
            base64.urlsafe_b64decode(payload_b64.encode("ascii")).decode("utf-8")
        )
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
        raise ValueError("Invalid JWT payload") from exc

    exp = payload.get("exp")
    if exp is None:
        raise ValueError("JWT payload does not contain 'exp' claim")

    try:
        exp = int(exp)
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid 'exp' claim") from exc

    return time.time() >= (exp + leeway)