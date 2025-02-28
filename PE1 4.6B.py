# Frequency Counter Function
def frequency_counter(data):
    return {item: data.count(item) for item in set(data)}  # Dictionary comprehension

# NATO Phonetic Alphabet Dictionary
NATO_ALPHABET = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
}

# NATO Phonetic Translation Function
def translation(word):
    return '\n'.join(NATO_ALPHABET[char] for char in word.upper())

# Example Usage
print(frequency_counter([1,1,2,1,3]))  # Output: {1:3, 2:1, 3:1}
print(translation("HELLO"))  
print(translation("APPLE"))
print(translation("GLASS"))