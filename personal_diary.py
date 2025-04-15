# personal_diary.py

def main():
    # Prompt the user to enter the current date and time
    date_time = input("Enter the current date and time")

    # Prompt the user to enter their diary entry
    entry = input("Enter your diary entry: ")

    # Open or create diary.txt in append mode
    diary_file = open("diary.txt", "a")

    # Write the entry to the file with a blank line after
    diary_file.write(f"{date_time}\n{entry}\n\n")

    # Close the file
    diary_file.close()

    print("Your entry has been saved to diary.txt!")

# Run the main function
if __name__ == "__main__":
    main()
