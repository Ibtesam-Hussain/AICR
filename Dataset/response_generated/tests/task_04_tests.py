import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_04_claude as claude_04
import gpt.task_04_gpt as gpt_04
import cursor.task_04_cursor as cursor_04

# Task 04: Write a function that extracts all email addresses from a block of text.

# Wrappers to normalize signatures
def claude_wrapper(text):
    return claude_04.extract_emails(text)

def gpt_wrapper(text):
    return gpt_04.extract_emails(text)

def cursor_wrapper(text):
    return cursor_04.extract_emails(text)

def test_task_04():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - text with multiple email addresses
    try:
        text = "Contact us at support@example.com or sales@example.com for help."
        expected = ['support@example.com', 'sales@example.com']
        
        claude_result = claude_wrapper(text)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(text)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(text)
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
        text = ""
        expected = []
        
        claude_result = claude_wrapper(text)
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(text)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(text)
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
        text = None
        
        claude_result = claude_wrapper(text)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (TypeError, AttributeError) as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(text)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (TypeError, AttributeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(text)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (TypeError, AttributeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single email
    try:
        text = "Email: test@example.com"
        expected = ['test@example.com']
        
        claude_result = claude_wrapper(text)
        assert claude_result == expected, f"Claude single: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(text)
        assert gpt_result == expected, f"GPT single: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(text)
        assert cursor_result == expected, f"Cursor single: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - duplicate emails (Cursor should dedupe, others may not)
    try:
        text = "Contact support@example.com or support@example.com for help."
        
        claude_result = claude_wrapper(text)
        # Claude and GPT return all matches including duplicates
        assert len(claude_result) == 2, f"Claude: Should return duplicate matches"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_wrapper(text)
        assert len(gpt_result) == 2, f"GPT: Should return duplicate matches"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_wrapper(text)
        # Cursor deduplicates
        assert len(cursor_result) == 1, f"Cursor: Should deduplicate emails"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (duplicates): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (duplicates): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (duplicates): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_04()
    print("Task 04 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
