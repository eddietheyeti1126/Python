import calendar  # Module to generate calendars
import datetime  # Module to get current year

def main():
    # Get the current year using datetime
    current_year = datetime.datetime.now().year

    try:
        # Ask the user for their birth month
        user_input = input("Enter your birth month as a number (1-12): ")
        birth_month = int(user_input)

        # Validate that the month is between 1 and 12
        if 1 <= birth_month <= 12:
            print(f"\n📅 Here is your birth month calendar for {current_year}:\n")
            
            # Print the calendar for the month and current year
            print(calendar.month(current_year, birth_month))
        else:
            print("⚠️ Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        # Handle non-integer input
        print("⚠️ Please enter a valid number.")

# Call the main function
if __name__ == "__main__":
    main()
