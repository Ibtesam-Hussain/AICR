import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_17_claude as claude_17
import gpt.task_17_gpt as gpt_17
import cursor.task_17_cursor as cursor_17

# Task 17: Write a function to find the second largest number in a list.

# Wrappers to normalize signatures
def claude_wrapper(numbers):
    return claude_17.second_largest(numbers)

def gpt_wrapper(numbers):
    return gpt_17.second_largest(numbers)

def cursor_wrapper(numbers):
    return cursor_17.second_largest(numbers)

def test_task_17():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - list with distinct numbers
    try:
        numbers = [1, 5, 3, 9, 2]
        expected = 5
        
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
    
    # Test 2: Empty/minimal input case - single element
    try:
        numbers = [5]
        
        claude_result = claude_wrapper(numbers)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (single): Should reject single element, got {claude_result}")
    except ValueError as e:
        results['claude']['passed'] += 1
    
    try:
        gpt_result = gpt_wrapper(numbers)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (single): Should reject single element, got {gpt_result}")
    except ValueError as e:
        results['gpt']['passed'] += 1
    
    try:
        cursor_result = cursor_wrapper(numbers)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (single): Should reject single element, got {cursor_result}")
    except ValueError as e:
        results['cursor']['passed'] += 1
    
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
    
    # Test 4: Boundary value case - list with duplicates
    try:
        numbers = [5, 5, 5, 3, 3]
        expected = 3
        
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
        results['claude']['errors'].append(f"Test 4 (duplicates): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (duplicates): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (duplicates): {str(e)}")
    
    # Test 5: Malformed/unusual input - list with all same values
    try:
        numbers = [5, 5, 5, 5]
        
        claude_result = claude_wrapper(numbers)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (all same): Should reject all same values, got {claude_result}")
    except ValueError as e:
        results['claude']['passed'] += 1
    
    try:
        gpt_result = gpt_wrapper(numbers)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (all same): Should reject all same values, got {gpt_result}")
    except ValueError as e:
        results['gpt']['passed'] += 1
    
    try:
        cursor_result = cursor_wrapper(numbers)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (all same): Should reject all same values, got {cursor_result}")
    except ValueError as e:
        results['cursor']['passed'] += 1
    
    return results

if __name__ == "__main__":
    results = test_task_17()
    print("Task 17 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
