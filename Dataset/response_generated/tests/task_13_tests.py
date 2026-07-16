import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')
import time
import base64
import json

import claude.task_13_claude as claude_13
import gpt.task_13_gpt as gpt_13
import cursor.task_13_cursor as cursor_13

# Task 13: Write a function that checks if a JWT-style token has expired based on its payload.

# Helper to create a test JWT token
def create_test_jwt(exp_time):
    payload = {"exp": exp_time}
    payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
    return f"header.{payload_b64}.signature"

# Wrappers to normalize signatures
def claude_wrapper(token):
    return claude_13.is_jwt_expired(token)

def gpt_wrapper(token):
    try:
        return gpt_13.is_jwt_expired(token)
    except ValueError:
        # GPT raises ValueError on invalid tokens
        return True  # Treat as expired

def cursor_wrapper(token):
    return cursor_13.is_jwt_expired(token)

def test_task_13():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - valid expired token
    try:
        past_time = time.time() - 3600  # 1 hour ago
        token = create_test_jwt(past_time)
        
        claude_result = claude_wrapper(token)
        assert claude_result == True, f"Claude: Expired token should return True"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(token)
        assert gpt_result == True, f"GPT: Expired token should return True"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(token)
        assert cursor_result == True, f"Cursor: Expired token should return True"
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
        token = ""
        
        claude_result = claude_wrapper(token)
        # Claude returns True for malformed tokens
        assert claude_result == True, f"Claude: Empty token should be treated as expired"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(token)
        # GPT raises ValueError for invalid format, wrapper converts to True
        assert gpt_result == True, f"GPT: Empty token should be treated as expired"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(token)
        # Cursor returns True for malformed tokens
        assert cursor_result == True, f"Cursor: Empty token should be treated as expired"
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
        token = None
        
        claude_result = claude_wrapper(token)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(token)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(token)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - token that expires exactly now
    try:
        now = time.time()
        token = create_test_jwt(now)
        
        claude_result = claude_wrapper(token)
        # Claude uses >= comparison, so exact now is expired
        assert claude_result == True, f"Claude: Token expiring now should be expired"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(token)
        assert gpt_result == True, f"GPT: Token expiring now should be expired"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(token)
        assert cursor_result == True, f"Cursor: Token expiring now should be expired"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - token without exp claim
    try:
        payload = {"sub": "user123"}
        payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
        token = f"header.{payload_b64}.signature"
        
        claude_result = claude_wrapper(token)
        # Claude returns True for tokens without exp
        assert claude_result == True, f"Claude: Token without exp should be treated as expired"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(token)
        # GPT raises ValueError for missing exp, wrapper converts to True
        assert gpt_result == True, f"GPT: Token without exp should be treated as expired"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(token)
        # Cursor returns True for tokens without exp
        assert cursor_result == True, f"Cursor: Token without exp should be treated as expired"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (no exp): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (no exp): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (no exp): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_13()
    print("Task 13 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
