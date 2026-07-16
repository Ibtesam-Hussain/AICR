# Task: Write a function that converts a UTC timestamp to a user's local time given their timezone.

from datetime import datetime
import pytz

def convert_utc_to_local(utc_timestamp, user_timezone):
    utc_time = datetime.utcfromtimestamp(utc_timestamp).replace(tzinfo=pytz.utc)
    local_tz = pytz.timezone(user_timezone)
    local_time = utc_time.astimezone(local_tz)
    return local_time
