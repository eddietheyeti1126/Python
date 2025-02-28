def iterate_dictionary(numbers):
    num_dict = {1: "one", 2: "two", 3: "three"}
    for num in numbers:
        print(num_dict.get(num, "Number not in dictionary"))

def check_if_positive(numbers):
    for num in numbers:
        print(num if num >= 0 else "not positive")

def division(numbers):
    for num in numbers:
        print(round(100 / num, 2) if num != 0 else "can't divide by zero")

# Example Usage
if __name__ == "__main__":
    iterate_dictionary([1, 3, 4])
    check_if_positive([3, 5, -1, -9, 4, 13, -2])
    division([100, 0, 2, 7])
