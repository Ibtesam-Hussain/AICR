import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')
from datetime import datetime

import claude.task_28_claude as claude_28
import gpt.task_28_gpt as gpt_28
import cursor.task_28_cursor as cursor_28

# Task 28: Write a function that converts a UTC timestamp to a user's local time given their timezone.

# Wrappers to normalize signatures
def claude_wrapper(utc_timestamp, timezone):
    return claude_28.utc_to_local(utc_timestamp, timezone)

def gpt_wrapper(utc_timestamp, timezone):
    return gpt_28.convert_utc_to_local(utc_timestamp, timezone)

def cursor_wrapper(utc_timestamp, timezone):
    # Cursor expects datetime object, not timestamp
    if isinstance(utc_timestamp, (int, float)):
        utc_timestamp = datetime.fromtimestamp(utc_timestamp)
    return cursor_28.utc_to_local(utc_timestamp, timezone)

def test_task_28():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - convert UTC timestamp to Eastern time
    try:
        utc_timestamp = 1699564800  # Nov 10, 2023 00:00:00 UTC
        timezone = 'US/Eastern'
        
        claude_result = claude_wrapper(utc_timestamp, timezone)
        assert claude_result is not None, f"Claude: Should return datetime"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(utc_timestamp, timezone)
        assert gpt_result is not None, f"GPT: Should return datetime"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(utc_timestamp, timezone)
        assert cursor_result is not None, f"Cursor: Should return datetime"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - timestamp 0 (epoch)
    try:
        utc_timestamp = 0
        timezone = 'UTC'
        
        claude_result = claude_wrapper(utc_timestamp, timezone)
        assert claude_result is not None, f"Claude epoch: Should return datetime"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(utc_timestamp, timezone)
        assert gpt_result is not None, f"GPT epoch: Should return datetime"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(utc_timestamp, timezone)
        assert cursor_result is not None, f"Cursor epoch: Should return datetime"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (epoch): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (epoch): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (epoch): {str(e)}")
    
    # Test 3: None/missing input case
    try:
        utc_timestamp = None
        timezone = 'US/Eastern'
        
        claude_result = claude_wrapper(utc_timestamp, timezone)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(utc_timestamp, timezone)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(utc_timestamp, timezone)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - invalid timezone
    try:
        utc_timestamp = 1699564800
        timezone = 'Invalid/Timezone'
        
        claude_result = claude_wrapper(utc_timestamp, timezone)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (invalid tz): Should reject invalid timezone, got {claude_result}")
    except Exception as e:
        results['claude']['passed'] += 1
    
    try:
        gpt_result = gpt_wrapper(utc_timestamp, timezone)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (invalid tz): Should reject invalid timezone, got {gpt_result}")
    except Exception as e:
        results['gpt']['passed'] += 1
    
    try:
        cursor_result = cursor_wrapper(utc_timestamp, timezone)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (invalid tz): Should reject invalid timezone, got {cursor_result}")
    except Exception as e:
        results['cursor']['passed'] += 1
    
    # Test 5: Malformed/unusual input - negative timestamp
    try:
        utc_timestamp = -3600  # 1 hour before epoch
        timezone = 'UTC'
        
        claude_result = claude_wrapper(utc_timestamp, timezone)
        assert claude_result is not None, f"Claude negative: Should return datetime"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(utc_timestamp, timezone)
        assert gpt_result is not None, f"GPT negative: Should return datetime"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(utc_timestamp, timezone)
        assert cursor_result is not None, f"Cursor negative: Should return datetime"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_28()
    print("Task 28 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
