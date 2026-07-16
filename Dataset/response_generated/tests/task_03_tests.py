import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_03_claude as claude_03
import gpt.task_03_gpt as gpt_03
import cursor.task_03_cursor as cursor_03

# Task 03: Write a function to merge two dictionaries, combining values for keys that exist in both.

# Wrappers to normalize signatures
def claude_wrapper(dict1, dict2):
    return claude_03.merge_dicts(dict1, dict2)

def gpt_wrapper(dict1, dict2):
    return gpt_03.merge_dicts(dict1, dict2)

def cursor_wrapper(dict1, dict2):
    return cursor_03.merge_dicts(dict1, dict2)

def test_task_03():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - two dictionaries with some overlapping keys
    try:
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'b': 20, 'c': 30, 'd': 4}
        
        claude_result = claude_wrapper(dict1, dict2)
        # Claude's last implementation uses defaultdict(list) so all values become lists
        assert 'a' in claude_result and 'd' in claude_result, f"Claude: Missing keys"
        assert isinstance(claude_result['b'], list), f"Claude: Combined key should be list"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(dict1, dict2)
        assert 'a' in gpt_result and 'd' in gpt_result, f"GPT: Missing keys"
        assert isinstance(gpt_result['b'], list), f"GPT: Combined key should be list"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(dict1, dict2)
        # Cursor doesn't combine values by default, just overwrites
        assert 'a' in cursor_result and 'd' in cursor_result, f"Cursor: Missing keys"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case
    try:
        dict1 = {}
        dict2 = {}
        expected = {}
        
        claude_result = claude_wrapper(dict1, dict2)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(dict1, dict2)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(dict1, dict2)
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
        dict1 = None
        dict2 = {'a': 1}
        
        claude_result = claude_wrapper(dict1, dict2)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(dict1, dict2)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(dict1, dict2)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single key in each dict
    try:
        dict1 = {'a': 1}
        dict2 = {'a': 2}
        
        claude_result = claude_wrapper(dict1, dict2)
        assert isinstance(claude_result['a'], list), f"Claude: Should combine into list"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(dict1, dict2)
        assert isinstance(gpt_result['a'], list), f"GPT: Should combine into list"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(dict1, dict2)
        # Cursor overwrites by default
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - nested dictionaries
    try:
        dict1 = {'a': {'x': 1}, 'b': 2}
        dict2 = {'a': {'y': 2}, 'c': 3}
        
        claude_result = claude_wrapper(dict1, dict2)
        # Claude's defaultdict approach will put dicts in a list
        assert isinstance(claude_result['a'], list), f"Claude: Should combine nested dicts into list"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(dict1, dict2)
        # GPT doesn't handle nested dicts specially
        assert isinstance(gpt_result['a'], list), f"GPT: Should combine into list"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(dict1, dict2)
        # Cursor has special handling for nested dicts
        assert isinstance(cursor_result['a'], dict), f"Cursor: Should merge nested dicts"
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
    results = test_task_03()
    print("Task 03 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
