import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_23_claude as claude_23
import gpt.task_23_gpt as gpt_23
import cursor.task_23_cursor as cursor_23

# Task 23: Write a function that returns the top K most frequent elements in a list.

# Wrappers to normalize signatures
def claude_wrapper(elements, k):
    return claude_23.top_k_frequent(elements, k)

def gpt_wrapper(elements, k):
    return gpt_23.top_k_frequent(elements, k)

def cursor_wrapper(elements, k):
    return cursor_23.top_k_frequent(elements, k)

def test_task_23():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - find top K frequent elements
    try:
        elements = [1, 1, 1, 2, 2, 3]
        k = 2
        result = claude_wrapper(elements, k)
        assert len(result) == k, f"Claude: Should return {k} elements"
        assert 1 in result, f"Claude: Should include most frequent element"
        results['claude']['passed'] += 1
        
        result = gpt_wrapper(elements, k)
        assert len(result) == k, f"GPT: Should return {k} elements"
        assert 1 in result, f"GPT: Should include most frequent element"
        results['gpt']['passed'] += 1
        
        result = cursor_wrapper(elements, k)
        assert len(result) == k, f"Cursor: Should return {k} elements"
        assert 1 in result, f"Cursor: Should include most frequent element"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - empty list with k=0
    try:
        elements = []
        k = 0
        expected = []
        
        claude_result = claude_wrapper(elements, k)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(elements, k)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(elements, k)
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
        elements = None
        k = 2
        
        claude_result = claude_wrapper(elements, k)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(elements, k)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(elements, k)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - k=0
    try:
        elements = [1, 2, 3]
        k = 0
        expected = []
        
        claude_result = claude_wrapper(elements, k)
        assert claude_result == expected, f"Claude zero: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(elements, k)
        assert gpt_result == expected, f"GPT zero: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(elements, k)
        assert cursor_result == expected, f"Cursor zero: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (zero): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (zero): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (zero): {str(e)}")
    
    # Test 5: Malformed/unusual input - negative k
    try:
        elements = [1, 2, 3]
        k = -5
        
        claude_result = claude_wrapper(elements, k)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (negative): Should reject negative k, got {claude_result}")
    except ValueError as e:
        results['claude']['passed'] += 1
    
    try:
        gpt_result = gpt_wrapper(elements, k)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (negative): Should reject negative k, got {gpt_result}")
    except Exception as e:
        results['gpt']['passed'] += 1
    
    try:
        cursor_result = cursor_wrapper(elements, k)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (negative): Should reject negative k, got {cursor_result}")
    except Exception as e:
        results['cursor']['passed'] += 1
    
    return results

if __name__ == "__main__":
    results = test_task_23()
    print("Task 23 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
