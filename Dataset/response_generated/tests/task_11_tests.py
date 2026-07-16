import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_11_claude as claude_11
import gpt.task_11_gpt as gpt_11
import cursor.task_11_cursor as cursor_11

# Task 11: Write a function that generates a short unique token for password reset links.

# Wrappers to normalize signatures
def claude_wrapper(length=32):
    return claude_11.generate_reset_token(length)

def gpt_wrapper(length=32):
    return gpt_11.generate_password_reset_token(length)

def cursor_wrapper(length=32):
    return cursor_11.generate_reset_token(length)

def test_task_11():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - generate token with default length
    try:
        claude_result = claude_wrapper()
        assert isinstance(claude_result, str), f"Claude: Expected string, got {type(claude_result)}"
        assert len(claude_result) > 0, f"Claude: Expected non-empty token"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper()
        assert isinstance(gpt_result, str), f"GPT: Expected string, got {type(gpt_result)}"
        assert len(gpt_result) > 0, f"GPT: Expected non-empty token"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper()
        assert isinstance(cursor_result, str), f"Cursor: Expected string, got {type(cursor_result)}"
        assert len(cursor_result) > 0, f"Cursor: Expected non-empty token"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - very short token
    try:
        claude_result = claude_wrapper(length=1)
        assert isinstance(claude_result, str), f"Claude short: Expected string"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(length=1)
        assert isinstance(gpt_result, str), f"GPT short: Expected string"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(length=1)
        assert isinstance(cursor_result, str), f"Cursor short: Expected string"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (short): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (short): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (short): {str(e)}")
    
    # Test 3: None/missing input case - None as length (should use default or fail gracefully)
    try:
        claude_result = claude_wrapper(length=None)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None length gracefully, got {claude_result}")
    except (TypeError, ValueError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None length - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(length=None)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None length gracefully, got {gpt_result}")
    except (TypeError, ValueError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None length - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(length=None)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None length gracefully, got {cursor_result}")
    except (TypeError, ValueError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None length - {str(e)}")
    
    # Test 4: Boundary value case - zero length
    try:
        claude_result = claude_wrapper(length=0)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (zero): Should handle zero length gracefully, got {claude_result}")
    except (TypeError, ValueError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (zero): Crashes on zero length - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(length=0)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (zero): Should handle zero length gracefully, got {gpt_result}")
    except (TypeError, ValueError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (zero): Crashes on zero length - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(length=0)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (zero): Should handle zero length gracefully, got {cursor_result}")
    except (TypeError, ValueError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (zero): Crashes on zero length - {str(e)}")
    
    # Test 5: Malformed/unusual input - negative length
    try:
        claude_result = claude_wrapper(length=-10)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): Should handle negative length gracefully, got {claude_result}")
    except (TypeError, ValueError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): Crashes on negative length - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(length=-10)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): Should handle negative length gracefully, got {gpt_result}")
    except (TypeError, ValueError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): Crashes on negative length - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(length=-10)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): Should handle negative length gracefully, got {cursor_result}")
    except (TypeError, ValueError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): Crashes on negative length - {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_11()
    print("Task 11 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
