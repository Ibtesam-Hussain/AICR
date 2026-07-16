# Task: Write a function that calculates someone's age given their birthdate.

from datetime import date

def calculate_age(birthdate: date) -> int:
    """
    Calculate age in years given a birthdate.
    
    Args:
        birthdate: A date object representing the person's birthdate
        
    Returns:
        Age in years as an integer
        
    Raises:
        ValueError: If birthdate is in the future
    """
    today = date.today()
    
    if birthdate > today:
        raise ValueError("Birthdate cannot be in the future")
    
    age = today.year - birthdate.year
    
    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age
