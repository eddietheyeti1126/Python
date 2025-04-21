import datetime  # Import datetime module to work with dates and times

def main():
    try:
        # Ask the user to input their birthday in YYYY-MM-DD format
        birthday_input = input("Enter your birthday (YYYY-MM-DD): ")

        # Convert the input string into a datetime object
        birthday = datetime.datetime.strptime(birthday_input, "%Y-%m-%d")

        # Get the current date and time
        now = datetime.datetime.now()

        # Calculate the difference between now and the birthday
        age_timedelta = now - birthday

        # Get total number of days from the timedelta
        total_days = age_timedelta.days

        # Estimate years by dividing total days by 365.25 (accounts for leap years)
        years = total_days // 365

        # Calculate remaining days after full years
        remaining_days_after_years = total_days % 365

        # Estimate months by dividing remaining days by 30 (approximate month)
        months = remaining_days_after_years // 30

        # Calculate weeks by dividing total days by 7
        weeks = total_days // 7

        # Total hours by multiplying days by 24
        hours = age_timedelta.total_seconds() // 3600

        # Total minutes by dividing total seconds by 60
        minutes = age_timedelta.total_seconds() // 60

        # Display results in a user-friendly format
        print("\n🔢 Your Age Details:")
        print(f"Years: {years}")
        print(f"Months (excluding full years): {months}")
        print(f"Weeks: {weeks}")
        print(f"Days: {total_days}")
        print(f"Hours: {int(hours):,}")
        print(f"Minutes: {int(minutes):,}")

    except ValueError:
        # Handle incorrect input formats
        print(" Invalid date format! Please enter your birthday as YYYY-MM-DD.")

if __name__ == "__main__":
    main()
