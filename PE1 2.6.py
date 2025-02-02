def budget_tracker():
    total_budget = float(input("Enter your total budget: $"))
    expenses = {}

    while True:
        category = input("\nEnter expense category (or 'done' to finish): ").strip()
        if category.lower() == "done":
            break
        amount = float(input(f"Enter amount spent on {category}: $"))
        expenses[category] = amount

    print("\n Budget Breakdown:")
    total_spent = sum(expenses.values())

    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f} ({(amount / total_budget) * 100:.2f}%)")

    print(f"\nTotal Spent: ${total_spent:.2f}")
    print(f"Remaining Budget: ${total_budget - total_spent:.2f}")

budget_tracker()
