import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_24_claude as claude_24
import gpt.task_24_gpt as gpt_24
import cursor.task_24_cursor as cursor_24

# Task 24: Write a function that converts a price string like "$1,234.56" into a float.

# Wrappers to normalize signatures
def claude_wrapper(price_string):
    return claude_24.parse_price(price_string)

def gpt_wrapper(price_string):
    return gpt_24.parse_price(price_string)

def cursor_wrapper(price_string):
    return cursor_24.parse_price(price_string)

def test_task_24():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - standard price string
    try:
        price_string = "$1,234.56"
        expected = 1234.56
        
        claude_result = claude_wrapper(price_string)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(price_string)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(price_string)
        assert cursor_result == expected, f"Cursor: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - empty string
    try:
        price_string = ""
        
        claude_result = claude_wrapper(price_string)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (empty): Should handle empty string gracefully, got {claude_result}")
    except ValueError as e:
        results['claude']['passed'] += 1
    
    try:
        gpt_result = gpt_wrapper(price_string)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (empty): Should handle empty string gracefully, got {gpt_result}")
    except ValueError as e:
        results['gpt']['passed'] += 1
    
    try:
        cursor_result = cursor_wrapper(price_string)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (empty): Should handle empty string gracefully, got {cursor_result}")
    except ValueError as e:
        results['cursor']['passed'] += 1
    
    # Test 3: None/missing input case
    try:
        price_string = None
        
        claude_result = claude_wrapper(price_string)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(price_string)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(price_string)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - price without cents
    try:
        price_string = "$1,234"
        expected = 1234.0
        
        claude_result = claude_wrapper(price_string)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(price_string)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(price_string)
        assert cursor_result == expected, f"Cursor: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - price without currency symbol
    try:
        price_string = "1,234.56"
        expected = 1234.56
        
        claude_result = claude_wrapper(price_string)
        assert claude_result == expected, f"Claude: Should handle price without $"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(price_string)
        assert gpt_result == expected, f"GPT: Should handle price without $"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(price_string)
        assert cursor_result == expected, f"Cursor: Should handle price without $"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (no symbol): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (no symbol): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (no symbol): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_24()
    print("Task 24 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
