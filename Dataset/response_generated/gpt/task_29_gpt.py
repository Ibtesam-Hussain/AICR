# Task: Write a function that truncates a string to a max length without cutting a word in half.

def truncate_string(s, max_length):
    if len(s) <= max_length:
        return s
    truncated = s[:max_length].rsplit(' ', 1)[0]
    return truncated if truncated else s[:max_length]
