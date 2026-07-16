import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_15_claude as claude_15
import gpt.task_15_gpt as gpt_15
import cursor.task_15_cursor as cursor_15

# Task 15: Write a function that retries a failing API call up to 3 times before giving up.

# Wrappers to normalize signatures
def claude_wrapper(func, *args, max_retries=3, delay=1, backoff=2, **kwargs):
    return claude_15.retry_api_call(func, *args, max_retries=max_retries, delay=delay, backoff=backoff, **kwargs)

def gpt_wrapper(func, *args, retries=3, delay=1.0, **kwargs):
    return gpt_15.retry_api_call(func, *args, retries=retries, delay=delay, **kwargs)

def cursor_wrapper(func, max_attempts=3, delay=1.0):
    # Cursor takes a callable with no args, so we need to wrap
    def wrapped():
        return func()
    return cursor_15.retry_api_call(wrapped, max_attempts=max_attempts, delay=delay)

def test_task_15():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - function succeeds on first try
    try:
        def success_func():
            return "success"
        
        claude_result = claude_wrapper(success_func)
        assert claude_result == "success", f"Claude: Should return success"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(success_func)
        assert gpt_result == "success", f"GPT: Should return success"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(success_func)
        assert cursor_result == "success", f"Cursor: Should return success"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - zero retries (should fail immediately)
    try:
        call_count = [0]
        def fail_func():
            call_count[0] += 1
            raise ValueError("Failed")
        
        claude_result = claude_wrapper(fail_func, max_retries=0, delay=0)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (zero retries): Should fail immediately, got {claude_result}")
    except ValueError:
        results['claude']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (zero retries): Unexpected error - {str(e)}")
    
    try:
        call_count = [0]
        def fail_func():
            call_count[0] += 1
            raise ValueError("Failed")
        
        gpt_result = gpt_wrapper(fail_func, retries=0, delay=0)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (zero retries): Should fail immediately, got {gpt_result}")
    except ValueError:
        results['gpt']['passed'] += 1
    except Exception as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (zero retries): Unexpected error - {str(e)}")
    
    try:
        call_count = [0]
        def fail_func():
            call_count[0] += 1
            raise ValueError("Failed")
        
        cursor_result = cursor_wrapper(fail_func, max_attempts=0, delay=0)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (zero retries): Should fail immediately, got {cursor_result}")
    except ValueError:
        results['cursor']['passed'] += 1
    except Exception as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (zero retries): Unexpected error - {str(e)}")
    
    # Test 3: None/missing input case - None as function
    try:
        claude_result = claude_wrapper(None)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None func): Should handle None function gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None func): Crashes on None function - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(None)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None func): Should handle None function gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None func): Crashes on None function - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(None)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None func): Should handle None function gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None func): Crashes on None function - {str(e)}")
    
    # Test 4: Boundary value case - succeeds on last retry
    try:
        call_count = [0]
        def succeed_on_third():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("Failed")
            return "success"
        
        claude_result = claude_wrapper(succeed_on_third, max_retries=3, delay=0)
        assert claude_result == "success", f"Claude: Should succeed on last retry"
        results['claude']['passed'] += 1
        
        call_count = [0]
        gpt_result = gpt_wrapper(succeed_on_third, retries=3, delay=0)
        assert gpt_result == "success", f"GPT: Should succeed on last retry"
        results['gpt']['passed'] += 1
        
        call_count = [0]
        cursor_result = cursor_wrapper(succeed_on_third, max_attempts=3, delay=0)
        assert cursor_result == "success", f"Cursor: Should succeed on last retry"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - negative retries
    try:
        def fail_func():
            raise ValueError("Failed")
        
        claude_result = claude_wrapper(fail_func, max_retries=-1, delay=0)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): Should handle negative retries gracefully, got {claude_result}")
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): Crashes on negative retries - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(fail_func, retries=-1, delay=0)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): Should handle negative retries gracefully, got {gpt_result}")
    except Exception as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): Crashes on negative retries - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(fail_func, max_attempts=-1, delay=0)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): Should handle negative attempts gracefully, got {cursor_result}")
    except Exception as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): Crashes on negative attempts - {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_15()
    print("Task 15 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
