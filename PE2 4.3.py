def main():
    # Change this path if your file is in a different location
    file_path = "sales_totals.txt"

    try:
        # Try to open the file in read mode
        with open(file_path, "r") as file:
            total = 0.0
            count = 0

            print("Sales amounts:\n")

            for line in file:
                line = line.strip()  # Remove newline and whitespace
                if line:  # Make sure the line is not empty
                    try:
                        amount = float(line)
                        print(f"${amount:,.2f}")
                        total += amount
                        count += 1
                    except ValueError:
                        print(f"Skipping invalid line: {line}")

            if count > 0:
                average = total / count
                print("\nSummary:")
                print(f"Total:   ${total:,.2f}")
                print(f"Count:   {count}")
                print(f"Average: ${average:,.2f}")
            else:
                print("No valid sales data found.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the script
if __name__ == "__main__":
    main()
