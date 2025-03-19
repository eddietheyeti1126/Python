def flowers(idx, list_of_flowers):
    """Selects a flower from a given list, handling potential errors."""
    try:
        # Ensure the index is an integer
        idx = int(idx)
        
        # Select the flower by index (handles negative indexing automatically)
        print(f"You selected: {list_of_flowers[idx]}")

    except ValueError:
        print("Invalid input! Please enter a number.")

    except IndexError:
        print("Number out of range! Please choose a valid flower number.")

flowers(1, ["Rose", "Lily", "Tulip"])  # You selected: Lily
flowers(5, ["Rose", "Lily", "Tulip"])  # Number out of range! Please choose a valid flower number.
flowers(-1, ["Rose", "Lily", "Tulip"])  # You selected: Tulip
flowers("one", ["Rose", "Lily", "Tulip"])  # Invalid input! Please enter a number.

