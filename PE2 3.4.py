class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind
        self._breed = breed
        self._name = name

    # Get methods
    def get_kind(self):
        return self._kind

    def get_breed(self):
        return self._breed

    def get_name(self):
        return self._name

    # Set methods
    def set_kind(self, kind):
        self._kind = kind

    def set_breed(self, breed):
        self._breed = breed

    def set_name(self, name):
        self._name = name

    # Print details method
    def print_details(self):
        print(f"Kind: {self._kind}, Breed: {self._breed}, Name: {self._name}")

# Creating instances
pet1 = Pet("Dog", "Golden Retriever", "Buddy")
pet2 = Pet("Cat", "Siamese", "Luna")
pet3 = Pet("Bird", "Parrot", "Kiwi")

# Calling print_details for each
pet1.print_details()
pet2.print_details()
pet3.print_details()

print("\n--- Special Methods / Functions Demonstration ---")

# Using type() to show class of an object
print("Type of pet1:", type(pet1))

# Using __module__ to show the module in which Pet class is defined
print("Module of Pet class:", Pet.__module__)

# Using __bases__ to show base classes of Pet class
print("Base classes of Pet:", Pet.__bases__)

# Using getattr() to access pet1's name
print("pet1's name using getattr():", getattr(pet1, "_name"))

# Using isinstance() to check if pet2 is an instance of Pet
print("Is pet2 an instance of Pet?", isinstance(pet2, Pet))
