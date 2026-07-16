# Task: Write a function that calculates someone's age given their birthdate.

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
