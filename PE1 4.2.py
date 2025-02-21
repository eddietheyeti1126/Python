def custom_song(animal, sound, place):
    print(f"\nOld MacDonald had a farm, E-I-E-I-O!")
    print(f"And on that {place} he had a {animal}, E-I-E-I-O!")
    print(f"With a {sound}-{sound} here and a {sound}-{sound} there,")
    print(f"Here a {sound}, there a {sound}, everywhere a {sound}-{sound}!")
    print("Old MacDonald had a farm, E-I-E-I-O!")

# Get user input
animal = input("Enter an animal: ")
sound = input("Enter the sound it makes: ")
place = input("Enter a place (farm, zoo, etc.): ")

# Call the function
custom_song(animal, sound, place)