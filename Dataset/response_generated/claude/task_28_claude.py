# Task: Write a function that converts a UTC timestamp to a user's local time given their timezone.

from datetime import datetime
import pytz

def utc_to_local(utc_timestamp: float, timezone: str) -> datetime:
    """
    Convert a UTC timestamp to local time in the specified timezone.
    
    Args:
        utc_timestamp: Unix timestamp (seconds since epoch)
        timezone: Timezone string (e.g., 'US/Eastern', 'Europe/London')
    
    Returns:
        datetime object in the specified timezone
    
    Raises:
        pytz.exceptions.UnknownTimeZoneError: If timezone is invalid
    """
    utc_dt = datetime.fromtimestamp(utc_timestamp, tz=pytz.UTC)
    local_tz = pytz.timezone(timezone)
    return utc_dt.astimezone(local_tz)

# Example: Convert current UTC time to Eastern time
timestamp = 1699564800  # Nov 10, 2023 00:00:00 UTC
local_time = utc_to_local(timestamp, 'US/Eastern')
print(local_time)  # 2023-11-09 19:00:00-05:00
