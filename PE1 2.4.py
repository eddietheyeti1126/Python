# Conversion functions
def inches_to_cm(inches):
    return inches * 2.54  # 1 inch = 2.54 cm

def feet_to_meters(feet):
    return feet * 0.3048  # 1 foot = 0.3048 meters

def pounds_to_kg(pounds):
    return pounds * 0.453592  # 1 pound = 0.453592 kg

def hours_to_minutes(hours):
    return hours * 60  # 1 hour = 60 minutes

# User input for conversion values
inches = float(input("Enter length in inches: "))
feet = float(input("Enter length in feet: "))
pounds = float(input("Enter weight in pounds: "))
hours = float(input("Enter time in hours: "))

# Perform conversions
cm_result = inches_to_cm(inches)
meters_result = feet_to_meters(feet)
kg_result = pounds_to_kg(pounds)
minutes_result = hours_to_minutes(hours)

# Display results
print("\nConversion Results:")
print(f"{inches} inches = {cm_result:.2f} centimeters")
print(f"{feet} feet = {meters_result:.2f} meters")
print(f"{pounds} pounds = {kg_result:.2f} kilograms")
print(f"{hours} hours = {minutes_result} minutes")
