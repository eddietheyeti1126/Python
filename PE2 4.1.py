# Generator function to yield all two-letter combinations
def two_letter_combinations(characters):
  
    for first in characters:
        for second in characters:
            yield first + second  # yield pauses and returns the combination

# Main function to run the generator
def main():
    # Define a 5-letter list of characters
    letters = ['a', 'b', 'c', 'd', 'e']

    print("Two-letter combinations:")
    # Call the generator and print each combination
    for combo in two_letter_combinations(letters):
        print(combo)

# Call the main function
main()
