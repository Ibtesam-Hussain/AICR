import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_06_claude as claude_06
import gpt.task_06_gpt as gpt_06
import cursor.task_06_cursor as cursor_06

# Task 06: Write a function that takes a list of numbers as strings and returns their sum.

# Wrappers to normalize signatures
def claude_wrapper(numbers):
    return claude_06.sum_numeric_strings(numbers)

def gpt_wrapper(numbers):
    return gpt_06.sum_string_numbers(numbers)

def cursor_wrapper(numbers):
    return cursor_06.sum_string_numbers(numbers)

def test_task_06():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - list of numeric strings
    try:
        numbers = ["1.5", "2.5", "3.0"]
        expected = 7.0
        
        claude_result = claude_wrapper(numbers)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(numbers)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(numbers)
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
        numbers = []
        expected = 0.0
        
        claude_result = claude_wrapper(numbers)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(numbers)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(numbers)
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
        numbers = None
        
        claude_result = claude_wrapper(numbers)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(numbers)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(numbers)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single number
    try:
        numbers = ["5.0"]
        expected = 5.0
        
        claude_result = claude_wrapper(numbers)
        assert claude_result == expected, f"Claude single: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(numbers)
        assert gpt_result == expected, f"GPT single: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(numbers)
        assert cursor_result == expected, f"Cursor single: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - non-numeric strings
    try:
        numbers = ["1.5", "abc", "3.0"]
        
        claude_result = claude_wrapper(numbers)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (malformed): Should handle non-numeric strings, got {claude_result}")
    except ValueError as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (malformed): Crashes on non-numeric string - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(numbers)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (malformed): Should handle non-numeric strings, got {gpt_result}")
    except ValueError as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (malformed): Crashes on non-numeric string - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(numbers)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (malformed): Should handle non-numeric strings, got {cursor_result}")
    except ValueError as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (malformed): Crashes on non-numeric string - {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_06()
    print("Task 06 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
