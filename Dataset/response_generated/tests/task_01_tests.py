import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')

import claude.task_01_claude as claude_01
import gpt.task_01_gpt as gpt_01
import cursor.task_01_cursor as cursor_01

# Task 01: Write a function that parses a CSV string and returns a list of dictionaries, one per row.

def test_task_01():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - valid CSV with headers and data
    try:
        csv_normal = "name,age,city\nJohn,30,New York\nJane,25,Los Angeles"
        expected = [{'name': 'John', 'age': '30', 'city': 'New York'}, {'name': 'Jane', 'age': '25', 'city': 'Los Angeles'}]
        
        claude_result = claude_01.parse_csv(csv_normal)
        assert claude_result == expected, f"Claude: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_01.parse_csv(csv_normal)
        assert gpt_result == expected, f"GPT: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_01.parse_csv(csv_normal)
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
        csv_empty = ""
        expected = []
        
        claude_result = claude_01.parse_csv(csv_empty)
        # Claude doesn't handle empty strings - will return empty list or raise error
        # Based on implementation, csv.DictReader on empty string returns empty
        assert claude_result == expected, f"Claude empty: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_01.parse_csv(csv_empty)
        assert gpt_result == expected, f"GPT empty: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_01.parse_csv(csv_empty)
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
        csv_none = None
        expected = []  # or could expect error handling
        
        claude_result = claude_01.parse_csv(csv_none)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {claude_result}")
    except (AttributeError, TypeError) as e:
        # Expected - None input should fail gracefully or be handled
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        gpt_result = gpt_01.parse_csv(csv_none)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {gpt_result}")
    except (AttributeError, TypeError) as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    try:
        cursor_result = cursor_01.parse_csv(csv_none)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Should handle None input gracefully, got {cursor_result}")
    except (AttributeError, TypeError) as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (None): Crashes on None input - {str(e)}")
    
    # Test 4: Boundary value case - single row (just header)
    try:
        csv_single = "name,age,city"
        expected = []  # No data rows, just header
        
        claude_result = claude_01.parse_csv(csv_single)
        assert claude_result == expected, f"Claude single: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_01.parse_csv(csv_single)
        assert gpt_result == expected, f"GPT single: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_01.parse_csv(csv_single)
        assert cursor_result == expected, f"Cursor single: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - CSV with quoted fields containing commas
    try:
        csv_quoted = 'name,age,city\n"John, Jr",30,"New York, NY"\nJane,25,Los Angeles'
        expected = [{'name': 'John, Jr', 'age': '30', 'city': 'New York, NY'}, {'name': 'Jane', 'age': '25', 'city': 'Los Angeles'}]
        
        claude_result = claude_01.parse_csv(csv_quoted)
        assert claude_result == expected, f"Claude quoted: Expected {expected}, got {claude_result}"
        results['claude']['passed'] += 1
        
        gpt_result = gpt_01.parse_csv(csv_quoted)
        assert gpt_result == expected, f"GPT quoted: Expected {expected}, got {gpt_result}"
        results['gpt']['passed'] += 1
        
        cursor_result = cursor_01.parse_csv(csv_quoted)
        assert cursor_result == expected, f"Cursor quoted: Expected {expected}, got {cursor_result}"
        results['cursor']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (quoted): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (quoted): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (quoted): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_01()
    print("Task 01 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
