import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_07_claude as claude_07
import gpt.task_07_gpt as gpt_07
import cursor.task_07_cursor as cursor_07

# Task 07: Write a function that deduplicates a list of dictionaries based on an "id" field.

# Wrappers to normalize signatures
def claude_wrapper(items):
    return claude_07.dedupe_by_id(items)

def gpt_wrapper(items):
    return gpt_07.deduplicate_by_id(items)

def cursor_wrapper(items):
    return cursor_07.deduplicate_by_id(items)

def test_task_07():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - list with duplicate IDs
    try:
        items = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}, {"id": 1, "name": "C"}]
        expected_len = 2  # Should dedupe based on id
        
        claude_result = claude_wrapper(items)
        assert len(claude_result) == expected_len, f"Claude: Expected {expected_len} items, got {len(claude_result)}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(items)
        assert len(gpt_result) == expected_len, f"GPT: Expected {expected_len} items, got {len(gpt_result)}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(items)
        assert len(cursor_result) == expected_len, f"Cursor: Expected {expected_len} items, got {len(cursor_result)}"
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
        items = []
        expected = []
        
        claude_result = claude_wrapper(items)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(items)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(items)
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
        items = None
        
        claude_result = claude_wrapper(items)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(items)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(items)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single item
    try:
        items = [{"id": 1, "name": "A"}]
        expected_len = 1
        
        claude_result = claude_wrapper(items)
        assert len(claude_result) == expected_len, f"Claude single: Expected {expected_len} item, got {len(claude_result)}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(items)
        assert len(gpt_result) == expected_len, f"GPT single: Expected {expected_len} item, got {len(gpt_result)}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(items)
        assert len(cursor_result) == expected_len, f"Cursor single: Expected {expected_len} item, got {len(cursor_result)}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - items missing "id" field
    try:
        items = [{"id": 1, "name": "A"}, {"name": "B"}, {"id": 1, "name": "C"}]
        
        claude_result = claude_wrapper(items)
        # Claude uses .get("id") which returns None for missing id
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(items)
        # GPT also uses .get("id")
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(items)
        # Cursor uses item["id"] which will crash on missing id
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (missing id): Should handle missing id gracefully, got {cursor_result}")
    except KeyError as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (missing id): Crashes on missing id field - {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_07()
    print("Task 07 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
