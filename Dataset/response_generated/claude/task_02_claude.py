from datetime import datetime
from dateutil import parser

def sort_dates(date_strings):
    return sorted(date_strings, key=parser.parse)