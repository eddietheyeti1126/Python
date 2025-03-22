def dictionary_exceptions(key, flower_dict):
    """Retrieves the price of a flower from the dictionary, handling KeyError exceptions."""
    try:
        print(f"The price of {key} is ${flower_dict[key]}")
    except KeyError:
        print("Error: Flower not found! Please enter Rose, Lily, or Tulip.")


def string_exceptions(idx, string):
    """Retrieves a character from a string at the given index, handling exceptions."""
    try:
        idx = int(idx)  # Convert to integer (handles ValueError if not a number)
        print(f"The character at index {idx} is: {string[idx]}")
    except ValueError:
        print("Error: Please enter a valid number for the index.")
    except IndexError:
        print("Error: Index out of range! Please enter a valid index.")
    except TypeError:
        print(f"Error: String indices must be integers, not '{type(idx).__name__}'")

# Dictionary Exception Handling Tests
dictionary_exceptions("Rose", {"Rose": 3.5, "Lily": 4.0, "Tulip": 2.5})  # The price of Rose is $3.5
dictionary_exceptions("Tulipia", {"Rose": 3.5, "Lily": 4.0, "Tulip": 2.5})  # Error: Flower not found!
dictionary_exceptions("", {"Rose": 3.5, "Lily": 4.0, "Tulip": 2.5})  # Error: Flower not found!
dictionary_exceptions("Lily", {"Rose": 3.5, "Lily": 4.0, "Tulip": 2.5})  # The price of Lily is $4.0

# String Exception Handling Tests
string_exceptions(4, "Hello World")  # The character at index 4 is: o
string_exceptions("abc", "Hello World")  # Error: String indices must be integers, not 'str'
string_exceptions(12, "Hello World")  # Error: Index out of range!
string_exceptions(0, "")  # Error: Index out of range!
