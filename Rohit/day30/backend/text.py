# utils/text.py
def count_words(text: str) -> int:
    return len([w for w in text.strip().split() if w])

def validate_remark_length(text: str, min_words: int = 200, max_words: int = 300):
    words = count_words(text)
    if words < min_words or words > max_words:
        return False, words
    return True, words
