def convert_to_ascii(text):
    if len(text) == 1:
        return ord(text)  # Return ASCII value for a single character
    return [ord(char) for char in text]  # Return ASCII values list for a string


def filter_non_ascii(text):
    return "".join(char for char in text if ord(char) < 128)

# Example Usage:
if __name__ == "__main__":
    print(convert_to_ascii("a"))  # Output: 97
    print(convert_to_ascii("Hello World"))  # Output: [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
    print(convert_to_ascii("C"))  # Output: 67
    print(filter_non_ascii("H" + chr(233) + "llo World"))  # Output: Hllo World
    print(filter_non_ascii("Hello World"))  # Output: Hello World
    print(filter_non_ascii("Y" + chr(233) + "s, This is for " + chr(255) + "ou"))  # Output: Ys, This is for ou
