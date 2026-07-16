def truncate_without_breaking_words(text: str, max_length: int) -> str:
    if len(text) <= max_length:
        return text

    truncated = text[:max_length].rstrip()
    last_space = truncated.rfind(" ")
    if last_space == -1:
        return truncated
    return truncated[:last_space].rstrip()
