def is_palindrome(string):
    # Normalize the string: remove spaces, convert to lowercase
    cleaned_string = ''.join(filter(str.isalnum, string.lower()))
    # Check if it reads the same forward and backward
    return cleaned_string == cleaned_string[::-1]


def is_anagram(string1, string2):
    # Normalize both strings: remove spaces, convert to lowercase, sort the characters
    cleaned_string1 = sorted(''.join(filter(str.isalnum, string1.lower())))
    cleaned_string2 = sorted(''.join(filter(str.isalnum, string2.lower())))
    # Check if sorted versions of both strings are identical
    return cleaned_string1 == cleaned_string2


# Example usage
if __name__ == "__main__":
    print(is_palindrome("hello"))  # False
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("rotator"))  # True

    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("night", "thing"))  # True
    print(is_anagram("hello", "world"))  # False
