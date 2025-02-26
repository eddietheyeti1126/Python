def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

def main(n):
    return f"The factorial of {n} is {factorial(n)}."

# Example usage
if __name__ == "__main__":
    print(main(5))  # Output: The factorial of 5 is 120.
    print(main(8))  # Output: The factorial of 8 is 40320.
