import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_19_claude as claude_19
import gpt.task_19_gpt as gpt_19
import cursor.task_19_cursor as cursor_19

# Task 19: Write a function that finds the longest increasing subsequence in a list of numbers.

# Wrappers to normalize signatures
def claude_wrapper(nums):
    return claude_19.longest_increasing_subsequence(nums)

def gpt_wrapper(nums):
    return gpt_19.longest_increasing_subsequence(nums)

def cursor_wrapper(nums):
    return cursor_19.longest_increasing_subsequence(nums)

def test_task_19():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - list with increasing subsequence
    try:
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        result = claude_wrapper(nums)
        assert len(result) > 0, f"Claude: Should return non-empty result"
        assert result == sorted(result), f"Claude: Result should be increasing"
        results['claude']['passed'] += 1
        
        result = gpt_wrapper(nums)
        assert len(result) > 0, f"GPT: Should return non-empty result"
        assert result == sorted(result), f"GPT: Result should be increasing"
        results['gpt']['passed'] += 1
        
        result = cursor_wrapper(nums)
        assert len(result) > 0, f"Cursor: Should return non-empty result"
        assert result == sorted(result), f"Cursor: Result should be increasing"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - empty list
    try:
        nums = []
        expected = []
        
        claude_result = claude_wrapper(nums)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(nums)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(nums)
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
        nums = None
        
        claude_result = claude_wrapper(nums)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(nums)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(nums)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single element
    try:
        nums = [5]
        expected = [5]
        
        claude_result = claude_wrapper(nums)
        assert claude_result == expected, f"Claude single: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(nums)
        assert gpt_result == expected, f"GPT single: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(nums)
        assert cursor_result == expected, f"Cursor single: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - all decreasing sequence
    try:
        nums = [5, 4, 3, 2, 1]
        result = claude_wrapper(nums)
        assert len(result) == 1, f"Claude: Should return single element for decreasing sequence"
        results['claude']['passed'] += 1
        
        result = gpt_wrapper(nums)
        assert len(result) == 1, f"GPT: Should return single element for decreasing sequence"
        results['gpt']['passed'] += 1
        
        result = cursor_wrapper(nums)
        assert len(result) == 1, f"Cursor: Should return single element for decreasing sequence"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (decreasing): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (decreasing): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (decreasing): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_19()
    print("Task 19 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
