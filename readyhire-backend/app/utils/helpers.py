import re

def clean_text(text: str) -> str:
    """
    Cleans up multiple spaces and newlines from a string.
    """
    if not text:
        return ""
    # Replace multiple spaces with a single space
    cleaned = re.sub(r'[ \t]+', ' ', text)
    # Replace multiple newlines with a single newline
    cleaned = re.sub(r'\n+', '\n', cleaned)
    return cleaned.strip()
