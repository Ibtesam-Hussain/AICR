import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_22_claude as claude_22
import gpt.task_22_gpt as gpt_22
import cursor.task_22_cursor as cursor_22

# Task 22: Write a recursive function to calculate the nth Fibonacci number.

# Wrappers to normalize signatures
def claude_wrapper(n):
    return claude_22.fibonacci(n)

def gpt_wrapper(n):
    return gpt_22.fibonacci(n)

def cursor_wrapper(n):
    return cursor_22.fibonacci(n)

def test_task_22():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - valid Fibonacci number
    try:
        n = 10
        expected = 55
        
        claude_result = claude_wrapper(n)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(n)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(n)
        assert cursor_result == expected, f"Cursor: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - n=0
    try:
        n = 0
        expected = 0
        
        claude_result = claude_wrapper(n)
        assert claude_result == expected, f"Claude zero: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(n)
        assert gpt_result == expected, f"GPT zero: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(n)
        assert cursor_result == expected, f"Cursor zero: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (zero): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (zero): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (zero): {str(e)}")
    
    # Test 3: None/missing input case
    try:
        n = None
        
        claude_result = claude_wrapper(n)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, ValueError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(n)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, ValueError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(n)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, ValueError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - n=1
    try:
        n = 1
        expected = 1
        
        claude_result = claude_wrapper(n)
        assert claude_result == expected, f"Claude one: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(n)
        assert gpt_result == expected, f"GPT one: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(n)
        assert cursor_result == expected, f"Cursor one: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - negative number
    try:
        n = -5
        
        claude_result = claude_wrapper(n)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): Should reject negative input, got {claude_result}")
    except ValueError as e:
        results['claude']['passed'] += 1
    
    try:
        gpt_result = gpt_wrapper(n)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): Should reject negative input, got {gpt_result}")
    except ValueError as e:
        results['gpt']['passed'] += 1
    
    try:
        cursor_result = cursor_wrapper(n)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): Should reject negative input, got {cursor_result}")
    except ValueError as e:
        results['cursor']['passed'] += 1
    
    return results

if __name__ == "__main__":
    results = test_task_22()
    print("Task 22 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
