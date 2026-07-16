import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_16_claude as claude_16
import gpt.task_16_gpt as gpt_16
import cursor.task_16_cursor as cursor_16

# Task 16: Write a function that masks sensitive fields (like credit card numbers) in a response dictionary before logging it.

# Wrappers to normalize signatures
def claude_wrapper(data, sensitive_keys=None, mask_char="*", visible_chars=4):
    return claude_16.mask_sensitive_fields(data, sensitive_keys=sensitive_keys, mask_char=mask_char, visible_chars=visible_chars)

def gpt_wrapper(data, sensitive_keys=None, mask="****"):
    return gpt_16.mask_sensitive_fields(data, sensitive_keys=sensitive_keys, mask=mask)

def cursor_wrapper(data):
    return cursor_16.mask_sensitive_fields(data)

def test_task_16():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - mask credit card number
    try:
        data = {"user": "john", "credit_card": "1234567890123456"}
        
        claude_result = claude_wrapper(data)
        assert claude_result["credit_card"] != "1234567890123456", f"Claude: Should mask credit card"
        assert "3456" in claude_result["credit_card"], f"Claude: Should show last 4 digits"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(data)
        assert gpt_result["credit_card"] == "****", f"GPT: Should mask with default mask"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(data)
        assert cursor_result["credit_card"] != "1234567890123456", f"Cursor: Should mask credit card"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - empty dict
    try:
        data = {}
        expected = {}
        
        claude_result = claude_wrapper(data)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(data)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(data)
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
        data = None
        
        claude_result = claude_wrapper(data)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(data)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(data)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - short sensitive value (shorter than visible chars)
    try:
        data = {"password": "123"}
        
        claude_result = claude_wrapper(data)
        assert claude_result["password"] == "***", f"Claude: Should mask short password completely"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(data)
        assert gpt_result["password"] == "****", f"GPT: Should mask with default mask"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(data)
        assert cursor_result["password"] != "123", f"Cursor: Should mask short password"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - nested dict with sensitive fields
    try:
        data = {"user": {"name": "john", "password": "secret123"}, "api_key": "abc123"}
        
        claude_result = claude_wrapper(data)
        assert claude_result["user"]["password"] != "secret123", f"Claude: Should mask nested password"
        assert claude_result["api_key"] != "abc123", f"Claude: Should mask api_key"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(data)
        assert gpt_result["user"]["password"] == "****", f"GPT: Should mask nested password"
        assert gpt_result["api_key"] == "****", f"GPT: Should mask api_key"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(data)
        assert cursor_result["user"]["password"] != "secret123", f"Cursor: Should mask nested password"
        assert cursor_result["api_key"] != "abc123", f"Cursor: Should mask api_key"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (nested): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (nested): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (nested): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_16()
    print("Task 16 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
