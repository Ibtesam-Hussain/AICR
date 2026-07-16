import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_10_claude as claude_10
import gpt.task_10_gpt as gpt_10
import cursor.task_10_cursor as cursor_10

# Task 10: Write a function that validates a user registration payload (email, password, age).

# Wrappers to normalize signatures and handle different return formats
def claude_wrapper(payload):
    is_valid, errors = claude_10.validate_registration(payload)
    # Claude returns (bool, list[str])
    return is_valid, errors

def gpt_wrapper(payload):
    is_valid, errors = gpt_10.validate_registration_payload(payload)
    # GPT returns (bool, list[str])
    return is_valid, errors

def cursor_wrapper(payload):
    is_valid, errors = cursor_10.validate_registration(payload)
    # Cursor returns (bool, dict[str, list[str]])
    # Convert to list format for consistency
    if isinstance(errors, dict):
        error_list = []
        for field, field_errors in errors.items():
            error_list.extend(field_errors)
        return is_valid, error_list
    return is_valid, errors

def test_task_10():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - valid registration payload
    try:
        payload = {"email": "test@example.com", "password": "Password123!", "age": 25}
        
        claude_result = claude_wrapper(payload)
        assert claude_result[0] == True, f"Claude: Expected valid payload"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(payload)
        assert gpt_result[0] == True, f"GPT: Expected valid payload"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(payload)
        assert cursor_result[0] == True, f"Cursor: Expected valid payload"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - missing all fields
    try:
        payload = {}
        
        claude_result = claude_wrapper(payload)
        assert claude_result[0] == False, f"Claude: Expected invalid payload"
        assert len(claude_result[1]) > 0, f"Claude: Expected error messages"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(payload)
        assert gpt_result[0] == False, f"GPT: Expected invalid payload"
        assert len(gpt_result[1]) > 0, f"GPT: Expected error messages"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(payload)
        assert cursor_result[0] == False, f"Cursor: Expected invalid payload"
        assert len(cursor_result[1]) > 0, f"Cursor: Expected error messages"
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
        payload = None
        
        claude_result = claude_wrapper(payload)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(payload)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(payload)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - age at minimum (13)
    try:
        payload = {"email": "test@example.com", "password": "Password123!", "age": 13}
        
        claude_result = claude_wrapper(payload)
        assert claude_result[0] == True, f"Claude: Age 13 should be valid"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(payload)
        assert gpt_result[0] == True, f"GPT: Age 13 should be valid"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(payload)
        assert cursor_result[0] == True, f"Cursor: Age 13 should be valid"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - invalid email format
    try:
        payload = {"email": "invalid-email", "password": "Password123!", "age": 25}
        
        claude_result = claude_wrapper(payload)
        assert claude_result[0] == False, f"Claude: Invalid email should fail"
        assert any("email" in err.lower() for err in claude_result[1]), f"Claude: Should have email error"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(payload)
        assert gpt_result[0] == False, f"GPT: Invalid email should fail"
        assert any("email" in err.lower() for err in gpt_result[1]), f"GPT: Should have email error"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(payload)
        assert cursor_result[0] == False, f"Cursor: Invalid email should fail"
        assert any("email" in err.lower() for err in cursor_result[1]), f"Cursor: Should have email error"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (malformed): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (malformed): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (malformed): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_10()
    print("Task 10 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
