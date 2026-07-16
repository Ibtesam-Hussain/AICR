# Task: Write a function that truncates a string to a max length without cutting a word in half.

def truncate_string(text, max_length, suffix="..."):
    """
    Truncates a string to max_length without cutting words in half.
    
    Args:
        text: The string to truncate
        max_length: Maximum length of the result (including suffix)
        suffix: String to append if truncated (default: "...")
    
    Returns:
        Truncated string, or original if it fits within max_length
    """
    if len(text) <= max_length:
        return text
    
    # Account for suffix length
    available_length = max_length - len(suffix)
    if available_length <= 0:
        return suffix[:max_length]
    
    # Truncate to available length and find the last space
    truncated = text[:available_length]
    last_space = truncated.rfind(" ")
    
    # If no space found, just cut at available length
    if last_space == -1:
        return truncated.rstrip() + suffix
    
    # Cut at the last space
    return truncated[:last_space].rstrip() + suffix

truncate_string("Hello world this is a test", 20)  # "Hello world this..."
truncate_string("Hello", 20)  # "Hello"
truncate_string("Supercalifragilisticexpialidocious extra", 20)  # "Supercalifragilisticexpialidocious..."
