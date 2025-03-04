import math

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

# Example usage
if __name__ == "__main__":
    print("Rectangle Area:", rectangle_area(5, 10))
    print("Triangle Area:", triangle_area(4, 6))
    print("Circle Area:", circle_area(7))
