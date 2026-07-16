import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_09_claude as claude_09
import gpt.task_09_gpt as gpt_09
import cursor.task_09_cursor as cursor_09

# Task 09: Write a function to paginate a list of items given a page number and page size.

# Wrappers to normalize signatures
def claude_wrapper(items, page, page_size):
    return claude_09.paginate(items, page, page_size)

def gpt_wrapper(items, page, page_size):
    return gpt_09.paginate(items, page, page_size)

def cursor_wrapper(items, page, page_size):
    return cursor_09.paginate(items, page, page_size)

def test_task_09():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - paginate a list
    try:
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        page = 2
        page_size = 3
        expected = [4, 5, 6]
        
        claude_result = claude_wrapper(items, page, page_size)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(items, page, page_size)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(items, page, page_size)
        assert cursor_result == expected, f"Cursor: Expected {expected}, got {cursor_result}"
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
        page = 1
        page_size = 10
        expected = []
        
        claude_result = claude_wrapper(items, page, page_size)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(items, page, page_size)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(items, page, page_size)
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
        page = 1
        page_size = 10
        
        claude_result = claude_wrapper(items, page, page_size)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(items, page, page_size)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(items, page, page_size)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - page beyond available data
    try:
        items = [1, 2, 3]
        page = 5
        page_size = 10
        expected = []
        
        claude_result = claude_wrapper(items, page, page_size)
        assert claude_result == expected, f"Claude boundary: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(items, page, page_size)
        assert gpt_result == expected, f"GPT boundary: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(items, page, page_size)
        assert cursor_result == expected, f"Cursor boundary: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - invalid page/page_size (negative or zero)
    try:
        items = [1, 2, 3, 4, 5]
        page = 0
        page_size = 10
        
        claude_result = claude_wrapper(items, page, page_size)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (invalid page): Should reject invalid page, got {claude_result}")
    except ValueError as e:
        # Expected - should validate input
        results['claude']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (invalid page): Unexpected error - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(items, page, page_size)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (invalid page): Should reject invalid page, got {gpt_result}")
    except ValueError as e:
        results['gpt']['passed'] += 1
    except Exception as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (invalid page): Unexpected error - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(items, page, page_size)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (invalid page): Should reject invalid page, got {cursor_result}")
    except ValueError as e:
        results['cursor']['passed'] += 1
    except Exception as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (invalid page): Unexpected error - {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_09()
    print("Task 09 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
