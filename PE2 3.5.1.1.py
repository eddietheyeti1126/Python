# Part 1: Class Definitions

class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    # Getters
    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    # Setters
    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)
        self._shift = shift
        self._pay_rate = pay_rate

    # Getters
    def get_shift(self):
        return self._shift

    def get_pay_rate(self):
        return self._pay_rate

    # Setters

    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate

        
    def set_shift(self, shift):
        self._shift = shift

    


# Part 2: User Interaction and Output

def main():
    print("Enter employee details:")

    name = input("Employee Name: ")
    number = input("Employee Number: ")
    shift = int(input("Shift Number (1 = Day, 2 = Night): "))
    pay_rate = float(input("Hourly Pay Rate: $"))

    # Create ProductionWorker instance
    worker = ProductionWorker(name, number, shift, pay_rate)

    # Display entered info
    print("\nEmployee Information:")
    print(f"Name: {worker.get_name()}")
    print(f"Number: {worker.get_number()}")
    print(f"Shift: {'Day' if worker.get_shift() == 1 else 'Night'}")
    print(f"Hourly Pay Rate: ${worker.get_pay_rate():.2f}")


if __name__ == "__main__":
    main()
