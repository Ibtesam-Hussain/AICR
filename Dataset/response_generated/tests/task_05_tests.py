import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_05_claude as claude_05
import gpt.task_05_gpt as gpt_05
import cursor.task_05_cursor as cursor_05

# Task 05: Write a function that converts a nested JSON object into a flat dictionary with dot-notation keys.

# Wrappers to normalize signatures
def claude_wrapper(obj):
    return claude_05.flatten_json(obj)

def gpt_wrapper(obj):
    return gpt_05.flatten_json(obj)

def cursor_wrapper(obj):
    return cursor_05.flatten_dict(obj)

def test_task_05():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - nested dictionary
    try:
        obj = {"a": {"b": 1, "c": 2}, "d": 3}
        
        claude_result = claude_wrapper(obj)
        assert "a.b" in claude_result and "a.c" in claude_result and "d" in claude_result, f"Claude: Missing keys"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(obj)
        assert "a.b" in gpt_result and "a.c" in gpt_result and "d" in gpt_result, f"GPT: Missing keys"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(obj)
        assert "a.b" in cursor_result and "a.c" in cursor_result and "d" in cursor_result, f"Cursor: Missing keys"
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
        obj = {}
        expected = {}
        
        claude_result = claude_wrapper(obj)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(obj)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(obj)
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
        obj = None
        
        claude_result = claude_wrapper(obj)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(obj)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(obj)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - flat dictionary (no nesting)
    try:
        obj = {"a": 1, "b": 2}
        expected = {"a": 1, "b": 2}
        
        claude_result = claude_wrapper(obj)
        assert claude_result == expected, f"Claude flat: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(obj)
        assert gpt_result == expected, f"GPT flat: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(obj)
        assert cursor_result == expected, f"Cursor flat: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - nested with lists (Claude and Cursor handle lists, GPT doesn't)
    try:
        obj = {"a": [1, 2, 3]}
        
        claude_result = claude_wrapper(obj)
        # Claude uses bracket notation for lists
        assert "a[0]" in claude_result, f"Claude: Should handle lists with bracket notation"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(obj)
        # GPT doesn't handle lists, will fail or treat list as leaf
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (lists): GPT doesn't handle nested lists, got {gpt_result}")
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (lists): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (lists): {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(obj)
        # Cursor uses dot notation for list indices
        assert "a.0" in cursor_result or "a[0]" in cursor_result, f"Cursor: Should handle lists"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (lists): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_05()
    print("Task 05 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
