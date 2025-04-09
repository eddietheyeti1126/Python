# Custom exception class
class NotNumericError(Exception):
    """Raised when input is not a numeric value."""
    pass

# Main program
def main():
    while True:
        try:
            user_input = input("Enter a number: ")
            if not user_input.isnumeric():
                raise NotNumericError("Input must be a number.")
        except NotNumericError as e:
            print(f"Error: {e}")
        else:
            print(f"Valid number entered: {user_input}")
            break
        finally:
            print("End of this attempt.\n")

# Run the program
if __name__ == "__main__":
    main()
