import random

def main(seed_value=None):
    if seed_value is not None:
        random.seed(seed_value)  # Set seed for testing consistency

    target_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))  # Take user input
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            difference = abs(target_number - guess)  # Calculate difference

            if difference == 0:
                print("You Got It!")
                break
            elif difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the main function
if __name__ == "__main__":
    main()
