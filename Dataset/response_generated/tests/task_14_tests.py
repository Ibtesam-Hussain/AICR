import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_14_claude as claude_14
import gpt.task_14_gpt as gpt_14
import cursor.task_14_cursor as cursor_14

# Task 14: Write a function that builds a query string from a dictionary of filter parameters.

# Wrappers to normalize signatures
def claude_wrapper(params):
    return claude_14.build_query_string(params)

def gpt_wrapper(params):
    return gpt_14.build_query_string(params)

def cursor_wrapper(params):
    return cursor_14.build_query_string(filters=params)

def test_task_14():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - build query string from dict
    try:
        params = {"name": "John", "age": "30", "city": "NYC"}
        
        claude_result = claude_wrapper(params)
        assert "name=John" in claude_result, f"Claude: Should contain name parameter"
        assert "age=30" in claude_result, f"Claude: Should contain age parameter"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(params)
        assert "name=John" in gpt_result, f"GPT: Should contain name parameter"
        assert "age=30" in gpt_result, f"GPT: Should contain age parameter"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(params)
        assert "name=John" in cursor_result, f"Cursor: Should contain name parameter"
        assert "age=30" in cursor_result, f"Cursor: Should contain age parameter"
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
        params = {}
        expected = ""
        
        claude_result = claude_wrapper(params)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(params)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(params)
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
        params = None
        
        claude_result = claude_wrapper(params)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(params)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(params)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single parameter
    try:
        params = {"key": "value"}
        
        claude_result = claude_wrapper(params)
        assert "key=value" in claude_result, f"Claude single: Should contain key=value"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(params)
        assert "key=value" in gpt_result, f"GPT single: Should contain key=value"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(params)
        assert "key=value" in cursor_result, f"Cursor single: Should contain key=value"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - params with None values (should be filtered)
    try:
        params = {"name": "John", "age": None, "city": "NYC"}
        
        claude_result = claude_wrapper(params)
        assert "name=John" in claude_result, f"Claude: Should contain name"
        assert "age" not in claude_result, f"Claude: Should filter out None values"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(params)
        assert "name=John" in gpt_result, f"GPT: Should contain name"
        assert "age" not in gpt_result, f"GPT: Should filter out None values"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(params)
        assert "name=John" in cursor_result, f"Cursor: Should contain name"
        assert "age" not in cursor_result, f"Cursor: Should filter out None values"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (None values): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (None values): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (None values): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_14()
    print("Task 14 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
