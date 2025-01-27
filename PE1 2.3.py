#Homework File
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Division by zero is not allowed."

#Equation
length = 10  
width = 5    

area = multiply(length, width)

print(f"The area of the rectangle with length {length} and width {width} is: {area}")