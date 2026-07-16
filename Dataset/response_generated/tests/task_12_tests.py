import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')
import time

import claude.task_12_claude as claude_12
import gpt.task_12_gpt as gpt_12
import cursor.task_12_cursor as cursor_12

# Task 12: Write a function to rate-limit API requests per user, allowing N requests per minute.

# Wrappers to normalize signatures
def claude_wrapper(max_requests, window_seconds=60):
    limiter = claude_12.RateLimiter(max_requests=max_requests, window_seconds=window_seconds)
    return limiter

def gpt_wrapper(max_requests, window_seconds=60):
    limiter = gpt_12.RateLimiter(max_requests=max_requests, window_seconds=window_seconds)
    return limiter

def cursor_wrapper(max_requests, per_seconds=60):
    limiter = cursor_12.create_rate_limiter(max_requests=max_requests, per_seconds=per_seconds)
    return limiter

def test_task_12():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - allow requests within limit
    try:
        claude_limiter = claude_wrapper(max_requests=3, window_seconds=60)
        assert claude_limiter.allow("user1") == True, f"Claude: First request should be allowed"
        assert claude_limiter.allow("user1") == True, f"Claude: Second request should be allowed"
        assert claude_limiter.allow("user1") == True, f"Claude: Third request should be allowed"
        results['claude']['passed'] += 1
        
        gpt_limiter = gpt_wrapper(max_requests=3, window_seconds=60)
        assert gpt_limiter.allow("user1") == True, f"GPT: First request should be allowed"
        assert gpt_limiter.allow("user1") == True, f"GPT: Second request should be allowed"
        assert gpt_limiter.allow("user1") == True, f"GPT: Third request should be allowed"
        results['gpt']['passed'] += 1
        
        cursor_limiter = cursor_wrapper(max_requests=3, per_seconds=60)
        assert cursor_limiter("user1") == True, f"Cursor: First request should be allowed"
        assert cursor_limiter("user1") == True, f"Cursor: Second request should be allowed"
        assert cursor_limiter("user1") == True, f"Cursor: Third request should be allowed"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - zero requests allowed
    try:
        claude_limiter = claude_wrapper(max_requests=0, window_seconds=60)
        assert claude_limiter.allow("user1") == False, f"Claude: Should deny when max_requests=0"
        results['claude']['passed'] += 1
        
        gpt_limiter = gpt_wrapper(max_requests=0, window_seconds=60)
        assert gpt_limiter.allow("user1") == False, f"GPT: Should deny when max_requests=0"
        results['gpt']['passed'] += 1
        
        cursor_limiter = cursor_wrapper(max_requests=0, per_seconds=60)
        assert cursor_limiter("user1") == False, f"Cursor: Should deny when max_requests=0"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (zero): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (zero): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (zero): {str(e)}")
    
    # Test 3: None/missing input case - None as user_id
    try:
        claude_limiter = claude_wrapper(max_requests=3, window_seconds=60)
        claude_result = claude_limiter.allow(None)
        # Should handle None user_id (may treat as valid string or fail)
        results['claude']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None user): Crashes on None user_id - {str(e)}")
    
    try:
        gpt_limiter = gpt_wrapper(max_requests=3, window_seconds=60)
        gpt_result = gpt_limiter.allow(None)
        results['gpt']['passed'] += 1
    except Exception as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None user): Crashes on None user_id - {str(e)}")
    
    try:
        cursor_limiter = cursor_wrapper(max_requests=3, per_seconds=60)
        cursor_result = cursor_limiter(None)
        results['cursor']['passed'] += 1
    except Exception as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None user): Crashes on None user_id - {str(e)}")
    
    # Test 4: Boundary value case - exactly at limit
    try:
        claude_limiter = claude_wrapper(max_requests=2, window_seconds=60)
        assert claude_limiter.allow("user1") == True, f"Claude: First request allowed"
        assert claude_limiter.allow("user1") == True, f"Claude: Second request allowed"
        assert claude_limiter.allow("user1") == False, f"Claude: Third request denied"
        results['claude']['passed'] += 1
        
        gpt_limiter = gpt_wrapper(max_requests=2, window_seconds=60)
        assert gpt_limiter.allow("user1") == True, f"GPT: First request allowed"
        assert gpt_limiter.allow("user1") == True, f"GPT: Second request allowed"
        assert gpt_limiter.allow("user1") == False, f"GPT: Third request denied"
        results['gpt']['passed'] += 1
        
        cursor_limiter = cursor_wrapper(max_requests=2, per_seconds=60)
        assert cursor_limiter("user1") == True, f"Cursor: First request allowed"
        assert cursor_limiter("user1") == True, f"Cursor: Second request allowed"
        assert cursor_limiter("user1") == False, f"Cursor: Third request denied"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - negative max_requests
    try:
        claude_limiter = claude_wrapper(max_requests=-5, window_seconds=60)
        claude_result = claude_limiter.allow("user1")
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): Should handle negative max_requests gracefully, got {claude_result}")
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): Crashes on negative max_requests - {str(e)}")
    
    try:
        gpt_limiter = gpt_wrapper(max_requests=-5, window_seconds=60)
        gpt_result = gpt_limiter.allow("user1")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): Should handle negative max_requests gracefully, got {gpt_result}")
    except Exception as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): Crashes on negative max_requests - {str(e)}")
    
    try:
        cursor_limiter = cursor_wrapper(max_requests=-5, per_seconds=60)
        cursor_result = cursor_limiter("user1")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): Should handle negative max_requests gracefully, got {cursor_result}")
    except Exception as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): Crashes on negative max_requests - {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_12()
    print("Task 12 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
