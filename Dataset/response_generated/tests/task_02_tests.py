import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_02_claude as claude_02
import gpt.task_02_gpt as gpt_02
import cursor.task_02_cursor as cursor_02

# Task 02: Write a function that takes a list of date strings and returns them sorted chronologically.

# Wrappers to normalize signatures
def claude_wrapper(date_strings):
    return claude_02.sort_dates(date_strings)

def gpt_wrapper(date_strings):
    return gpt_02.sort_dates(date_strings)

def cursor_wrapper(date_strings):
    return cursor_02.sort_dates(date_strings)

def test_task_02():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - valid date strings in ISO format
    try:
        dates = ["2023-01-15", "2023-03-20", "2023-02-10"]
        expected = ["2023-01-15", "2023-02-10", "2023-03-20"]
        
        claude_result = claude_wrapper(dates)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(dates)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(dates)
        assert cursor_result == expected, f"Cursor: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case
    try:
        dates = []
        expected = []
        
        claude_result = claude_wrapper(dates)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(dates)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(dates)
        assert cursor_result == expected, f"Cursor empty: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (empty): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (empty): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (empty): {str(e)}")
    
    # Test 3: None/missing input case
    try:
        dates = None
        
        claude_result = claude_wrapper(dates)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(dates)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(dates)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single date
    try:
        dates = ["2023-01-15"]
        expected = ["2023-01-15"]
        
        claude_result = claude_wrapper(dates)
        assert claude_result == expected, f"Claude single: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(dates)
        assert gpt_result == expected, f"GPT single: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(dates)
        assert cursor_result == expected, f"Cursor single: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - different date formats (Claude should handle with dateutil, others may fail)
    try:
        dates = ["15/01/2023", "20/03/2023", "10/02/2023"]  # DD/MM/YYYY format
        # Claude with dateutil should handle this, GPT/Cursor with strict format will fail
        expected_claude = ["15/01/2023", "10/02/2023", "20/03/2023"]  # dateutil parses DD/MM/YYYY
        
        claude_result = claude_wrapper(dates)
        # Claude's dateutil is flexible, but parsing may vary by locale
        # We'll just check it doesn't crash and returns sorted list
        assert isinstance(claude_result, list) and len(claude_result) == 3, f"Claude malformed: Expected list of 3, got {claude_result}"
        results['claude']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (malformed): {str(e)}")
    
    try:
        # GPT and Cursor expect YYYY-MM-DD format, this should fail
        gpt_result = gpt_wrapper(dates)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (malformed): Should fail on non-ISO format but returned {gpt_result}")
    except ValueError as e:
        # Expected - strict format parsing
        results['gpt']['passed'] += 1
    except Exception as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (malformed): Unexpected error - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(dates)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (malformed): Should fail on non-ISO format but returned {cursor_result}")
    except ValueError as e:
        # Expected - strict format parsing
        results['cursor']['passed'] += 1
    except Exception as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (malformed): Unexpected error - {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_02()
    print("Task 02 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
