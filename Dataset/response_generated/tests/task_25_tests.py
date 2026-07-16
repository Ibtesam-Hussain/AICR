import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')
from datetime import date

import claude.task_25_claude as claude_25
import gpt.task_25_gpt as gpt_25
import cursor.task_25_cursor as cursor_25

# Task 25: Write a function that calculates someone's age given their birthdate.

# Wrappers to normalize signatures
def claude_wrapper(birthdate):
    return claude_25.calculate_age(birthdate)

def gpt_wrapper(birthdate):
    # GPT expects string in YYYY-MM-DD format
    if isinstance(birthdate, date):
        birthdate_str = birthdate.strftime('%Y-%m-%d')
        return gpt_25.calculate_age(birthdate_str)
    return gpt_25.calculate_age(birthdate)

def cursor_wrapper(birthdate):
    return cursor_25.calculate_age(birthdate)

def test_task_25():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - valid birthdate
    try:
        birthdate = date(1990, 5, 15)
        today = date.today()
        expected_age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        claude_result = claude_wrapper(birthdate)
        assert claude_result == expected_age, f"Claude: Expected {expected_age}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(birthdate)
        assert gpt_result == expected_age, f"GPT: Expected {expected_age}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(birthdate)
        assert cursor_result == expected_age, f"Cursor: Expected {expected_age}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - very recent birthdate
    try:
        birthdate = date.today()
        expected = 0
        
        claude_result = claude_wrapper(birthdate)
        assert claude_result == expected, f"Claude today: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(birthdate)
        assert gpt_result == expected, f"GPT today: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(birthdate)
        assert cursor_result == expected, f"Cursor today: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (today): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (today): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (today): {str(e)}")
    
    # Test 3: None/missing input case
    try:
        birthdate = None
        
        claude_result = claude_wrapper(birthdate)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(birthdate)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError, ValueError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(birthdate)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - birthdate exactly one year ago
    try:
        birthdate = date(date.today().year - 1, date.today().month, date.today().day)
        expected = 1
        
        claude_result = claude_wrapper(birthdate)
        assert claude_result == expected, f"Claude boundary: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(birthdate)
        assert gpt_result == expected, f"GPT boundary: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(birthdate)
        assert cursor_result == expected, f"Cursor boundary: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - future birthdate
    try:
        birthdate = date(date.today().year + 10, 1, 1)
        
        claude_result = claude_wrapper(birthdate)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (future): Should reject future birthdate, got {claude_result}")
    except ValueError as e:
        results['claude']['passed'] += 1
    
    try:
        gpt_result = gpt_wrapper(birthdate)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (future): Should reject future birthdate, got {gpt_result}")
    except Exception as e:
        results['gpt']['passed'] += 1
    
    try:
        cursor_result = cursor_wrapper(birthdate)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (future): Should reject future birthdate, got {cursor_result}")
    except Exception as e:
        results['cursor']['passed'] += 1
    
    return results

if __name__ == "__main__":
    results = test_task_25()
    print("Task 25 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
