def group_by_first_letter(words):
    """Groups words by their first letter into a dictionary."""
    grouped = {}
    for word in words:
        first_letter = word[0].lower()
        grouped.setdefault(first_letter, []).append(word)
    return grouped


def convert_to_sentence(words):
    """Converts a list of words into a sentence with proper punctuation."""
    return " ".join(words) + "."

print(group_by_first_letter(["apple", "banana", "apricot", "blueberry", "cherry"]))
# Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

print(group_by_first_letter(["date", "dragonfruit", "durian", "grape", "grapefruit", "guava", "mango", "melon", "mulberry"]))
# Output: {'d': ['date', 'dragonfruit', 'durian'], 'g': ['grape', 'grapefruit', 'guava'], 'm': ['mango', 'melon', 'mulberry']}

print(group_by_first_letter(["broccoli", "beetroot", "butternut", "garlic", "ginger", "greenbean", "papaya", "pineapple", "pumpkin"]))
# Output: {'b': ['broccoli', 'beetroot', 'butternut'], 'g': ['garlic', 'ginger', 'greenbean'], 'p': ['papaya', 'pineapple', 'pumpkin']}

print(convert_to_sentence(["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]))
# Output: 'The quick brown fox jumps over the lazy dog.'

print(convert_to_sentence(["Learning", "Python", "is", "fun", "and", "challenging", "but", "rewarding"]))
# Output: 'Learning Python is fun and challenging but rewarding.'
