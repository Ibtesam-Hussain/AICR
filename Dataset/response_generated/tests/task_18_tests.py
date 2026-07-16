import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_18_claude as claude_18
import gpt.task_18_gpt as gpt_18
import cursor.task_18_cursor as cursor_18

# Task 18: Write a function that checks if two strings are anagrams of each other.

# Wrappers to normalize signatures
def claude_wrapper(s1, s2):
    return claude_18.is_anagram(s1, s2)

def gpt_wrapper(s1, s2):
    return gpt_18.are_anagrams(s1, s2)

def cursor_wrapper(s1, s2):
    return cursor_18.are_anagrams(s1, s2)

def test_task_18():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - valid anagrams
    try:
        s1 = "listen"
        s2 = "silent"
        
        claude_result = claude_wrapper(s1, s2)
        assert claude_result == True, f"Claude: Should be anagram"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(s1, s2)
        assert gpt_result == True, f"GPT: Should be anagram"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(s1, s2)
        assert cursor_result == True, f"Cursor: Should be anagram"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - empty strings
    try:
        s1 = ""
        s2 = ""
        
        claude_result = claude_wrapper(s1, s2)
        assert claude_result == True, f"Claude: Empty strings should be anagrams"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(s1, s2)
        assert gpt_result == True, f"GPT: Empty strings should be anagrams"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(s1, s2)
        assert cursor_result == True, f"Cursor: Empty strings should be anagrams"
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
        s1 = None
        s2 = "test"
        
        claude_result = claude_wrapper(s1, s2)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(s1, s2)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(s1, s2)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single character
    try:
        s1 = "a"
        s2 = "a"
        
        claude_result = claude_wrapper(s1, s2)
        assert claude_result == True, f"Claude: Single char should be anagram"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(s1, s2)
        assert gpt_result == True, f"GPT: Single char should be anagram"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(s1, s2)
        assert cursor_result == True, f"Cursor: Single char should be anagram"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - strings with spaces (Claude/GPT handle, Cursor may not)
    try:
        s1 = "eat"
        s2 = "e at"
        
        claude_result = claude_wrapper(s1, s2)
        assert claude_result == True, f"Claude: Should handle spaces"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(s1, s2)
        assert gpt_result == True, f"GPT: Should handle spaces"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(s1, s2)
        # Cursor doesn't remove spaces, so these won't be anagrams
        assert cursor_result == False, f"Cursor: Doesn't handle spaces, should be False"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (spaces): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (spaces): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (spaces): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_18()
    print("Task 18 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
