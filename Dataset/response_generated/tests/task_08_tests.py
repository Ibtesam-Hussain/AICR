import sys
sys.path.insert(0, 'c:\\Users\\MCA\\Desktop\\response_generated')
import tempfile
import os

import claude.task_08_claude as claude_08
import gpt.task_08_gpt as gpt_08
import cursor.task_08_cursor as cursor_08

# Task 08: Write a function that parses a log file and counts how many times each error type appears.

# Wrappers to normalize signatures
def claude_wrapper(file_path):
    return claude_08.count_error_types(file_path)

def gpt_wrapper(file_path):
    return gpt_08.count_error_types(log_file_path=file_path)

def cursor_wrapper(file_path):
    return cursor_08.count_error_types(log_path=file_path)

def test_task_08():
    results = {
        'claude': {'passed': 0, 'failed': 0, 'errors': []},
        'gpt': {'passed': 0, 'failed': 0, 'errors': []},
        'cursor': {'passed': 0, 'failed': 0, 'errors': []}
    }
    
    # Test 1: Normal case - log file with error messages
    try:
        log_content = """2026-07-15 10:30:12 ERROR DatabaseError: Connection failed
2026-07-15 10:31:00 ERROR ValueError: Invalid input
2026-07-15 10:32:00 ERROR DatabaseError: Timeout
2026-07-15 10:33:00 INFO System started"""
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
            f.write(log_content)
            temp_file = f.name
        
        try:
            claude_result = claude_wrapper(temp_file)
            # Claude uses regex to find error types
            assert len(claude_result) > 0, f"Claude: Should find error types"
            results['claude']['passed'] += 1
            
            gpt_result = gpt_wrapper(temp_file)
            # GPT looks for "ERROR" keyword
            assert len(gpt_result) > 0, f"GPT: Should find error types"
            results['gpt']['passed'] += 1
            
            cursor_result = cursor_wrapper(temp_file)
            # Cursor uses regex for ERROR/FATAL/CRITICAL
            assert len(cursor_result) > 0, f"Cursor: Should find error types"
            results['cursor']['passed'] += 1
        finally:
            os.unlink(temp_file)
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 1 (normal): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 1 (normal): {str(e)}")
    
    # Test 2: Empty/minimal input case - empty log file
    try:
        log_content = ""
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
            f.write(log_content)
            temp_file = f.name
        
        try:
            claude_result = claude_wrapper(temp_file)
            assert len(claude_result) == 0, f"Claude empty: Expected no errors"
            results['claude']['passed'] += 1
            
            gpt_result = gpt_wrapper(temp_file)
            assert len(gpt_result) == 0, f"GPT empty: Expected no errors"
            results['gpt']['passed'] += 1
            
            cursor_result = cursor_wrapper(temp_file)
            assert len(cursor_result) == 0, f"Cursor empty: Expected no errors"
            results['cursor']['passed'] += 1
        finally:
            os.unlink(temp_file)
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 2 (empty): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 2 (empty): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 2 (empty): {str(e)}")
    
    # Test 3: None/missing input case - non-existent file
    try:
        temp_file = "nonexistent_file.log"
        
        claude_result = claude_wrapper(temp_file)
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (missing file): Should handle missing file gracefully, got {claude_result}")
    except FileNotFoundError as e:
        # Claude explicitly raises FileNotFoundError
        results['claude']['passed'] += 1
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 3 (missing file): Unexpected error - {str(e)}")
    
    try:
        gpt_result = gpt_wrapper(temp_file)
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (missing file): Should handle missing file gracefully, got {gpt_result}")
    except FileNotFoundError as e:
        results['gpt']['passed'] += 1
    except Exception as e:
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 3 (missing file): Unexpected error - {str(e)}")
    
    try:
        cursor_result = cursor_wrapper(temp_file)
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (missing file): Should handle missing file gracefully, got {cursor_result}")
    except FileNotFoundError as e:
        results['cursor']['passed'] += 1
    except Exception as e:
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 3 (missing file): Unexpected error - {str(e)}")
    
    # Test 4: Boundary value case - single error line
    try:
        log_content = "2026-07-15 10:30:12 ERROR DatabaseError: Connection failed"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
            f.write(log_content)
            temp_file = f.name
        
        try:
            claude_result = claude_wrapper(temp_file)
            assert len(claude_result) > 0, f"Claude single: Should find error type"
            results['claude']['passed'] += 1
            
            gpt_result = gpt_wrapper(temp_file)
            assert len(gpt_result) > 0, f"GPT single: Should find error type"
            results['gpt']['passed'] += 1
            
            cursor_result = cursor_wrapper(temp_file)
            assert len(cursor_result) > 0, f"Cursor single: Should find error type"
            results['cursor']['passed'] += 1
        finally:
            os.unlink(temp_file)
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 4 (boundary): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 4 (boundary): {str(e)}")
    
    # Test 5: Malformed/unusual input - log without ERROR keyword (GPT may fail)
    try:
        log_content = """2026-07-15 10:30:12 DatabaseError: Connection failed
2026-07-15 10:31:00 ValueError: Invalid input"""
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
            f.write(log_content)
            temp_file = f.name
        
        try:
            claude_result = claude_wrapper(temp_file)
            # Claude uses regex pattern for Error/Exception, should still work
            assert len(claude_result) > 0, f"Claude malformed: Should find error types"
            results['claude']['passed'] += 1
            
            gpt_result = gpt_wrapper(temp_file)
            # GPT looks for "ERROR" keyword specifically
            if len(gpt_result) == 0:
                results['gpt']['failed'] += 1
                results['gpt']['errors'].append(f"Test 5 (no ERROR keyword): GPT requires ERROR keyword, found none")
            else:
                results['gpt']['passed'] += 1
            
            cursor_result = cursor_wrapper(temp_file)
            # Cursor looks for ERROR/FATAL/CRITICAL keywords
            if len(cursor_result) == 0:
                results['cursor']['failed'] += 1
                results['cursor']['errors'].append(f"Test 5 (no ERROR keyword): Cursor requires ERROR/FATAL/CRITICAL keyword, found none")
            else:
                results['cursor']['passed'] += 1
        finally:
            os.unlink(temp_file)
    except Exception as e:
        results['claude']['failed'] += 1
        results['claude']['errors'].append(f"Test 5 (malformed): {str(e)}")
        results['gpt']['failed'] += 1
        results['gpt']['errors'].append(f"Test 5 (malformed): {str(e)}")
        results['cursor']['failed'] += 1
        results['cursor']['errors'].append(f"Test 5 (malformed): {str(e)}")
    
    return results

if __name__ == "__main__":
    results = test_task_08()
    print("Task 08 Test Results:")
    for tool in ['claude', 'gpt', 'cursor']:
        print(f"  {tool}: passed={results[tool]['passed']}, failed={results[tool]['failed']}")
        if results[tool]['errors']:
            for err in results[tool]['errors']:
                print(f"    - {err}")
