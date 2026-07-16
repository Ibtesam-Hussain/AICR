from datetime import datetime
from zoneinfo import ZoneInfo


def utc_to_local(utc_timestamp: datetime, timezone: str) -> datetime:
    if utc_timestamp.tzinfo is None:
        utc_timestamp = utc_timestamp.replace(tzinfo=ZoneInfo("UTC"))
    return utc_timestamp.astimezone(ZoneInfo(timezone))
