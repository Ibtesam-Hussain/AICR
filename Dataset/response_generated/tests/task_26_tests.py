import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_26_claude as claude_26
import gpt.task_26_gpt as gpt_26
import cursor.task_26_cursor as cursor_26

# Task 26: Write a function that rounds a number to 2 decimal places for currency display.

# Wrappers to normalize signatures
def claude_wrapper(amount):
    # Claude has duplicate function definitions, use the last one (string format)
    # But for consistency with other tools, we'll test the float version
    return claude_26.format_currency(amount)

def gpt_wrapper(amount):
    return gpt_26.round_currency(amount)

def cursor_wrapper(amount):
    return cursor_26.round_currency(amount)

def test_task_26():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - round to 2 decimal places
    try:
        amount = 123.4567
        expected = 123.46
        
        claude_result = claude_wrapper(amount)
        # Claude's last definition returns string, so we need to handle that
        if isinstance(claude_result, str):
            claude_result = float(claude_result)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(amount)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(amount)
        assert cursor_result == expected, f"Cursor: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - zero
    try:
        amount = 0.0
        expected = 0.0
        
        claude_result = claude_wrapper(amount)
        if isinstance(claude_result, str):
            claude_result = float(claude_result)
        assert claude_result == expected, f"Claude zero: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(amount)
        assert gpt_result == expected, f"GPT zero: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(amount)
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
        amount = None
        
        claude_result = claude_wrapper(amount)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(amount)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(amount)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - negative number
    try:
        amount = -123.4567
        expected = -123.46
        
        claude_result = claude_wrapper(amount)
        if isinstance(claude_result, str):
            claude_result = float(claude_result)
        assert claude_result == expected, f"Claude negative: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(amount)
        assert gpt_result == expected, f"GPT negative: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(amount)
        assert cursor_result == expected, f"Cursor negative: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (negative): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (negative): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (negative): {str(e)}")
    
    # Test 5: Malformed/unusual input - string instead of number
    try:
        amount = "123.45"
        
        claude_result = claude_wrapper(amount)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (string): Should handle string input gracefully, got {claude_result}")
    except (TypeError, ValueError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (string): Crashes on string input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(amount)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (string): Should handle string input gracefully, got {gpt_result}")
    except (TypeError, ValueError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (string): Crashes on string input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(amount)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (string): Should handle string input gracefully, got {cursor_result}")
    except (TypeError, ValueError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (string): Crashes on string input - {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_26()
    print("Task 26 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
