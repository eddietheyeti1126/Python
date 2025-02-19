# Global constants for conversion
POUNDS_TO_KG = 0.453592  # 1 pound = 0.453592 kg
INCHES_TO_METERS = 0.0254  # 1 inch = 0.0254 meters

def bmi_calculation():
    
    while True:
        try:
            # Get user input for weight and height
            weight_pounds = float(input("Enter your weight in pounds: "))
            height_inches = float(input("Enter your height in inches: "))
            
            # Check if inputs are positive
            if weight_pounds <= 0 or height_inches <= 0:
                print("Weight and height must be positive numbers. Please try again.")
                continue
            
            # Convert weight and height to metric units
            weight_kg = weight_pounds * POUNDS_TO_KG
            height_m = height_inches * INCHES_TO_METERS
            
            # Calculate BMI
            bmi = weight_kg / (height_m ** 2)
            
            # Determine BMI category
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"
            
            # Display results
            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"Category: {category}")
            break 
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the BMI calculator
if __name__ == "__main__":
    bmi_calculation()
