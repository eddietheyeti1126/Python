# Rectangle Formula
def rectangle(side1, side2):
    return f'The area of the rectangle is {side1 * side2} square units'

# Circle Formula
def circle(radius):
    return f'The area of the circle is {3.14 * radius * radius} square units'

# Test cases
if __name__ == "__main__":
    print(rectangle(3, 4))
    print(rectangle(10, 5))
    print(circle(3))
    print(circle(5))
      
