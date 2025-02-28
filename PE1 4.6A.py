import math

def pythagorean_thm(sides):
    return round(math.hypot(*sides), 2)  # Uses formula

# Example usage
print(pythagorean_thm((3, 4)))    # Output: 5
print(pythagorean_thm((26, 91)))  # Output: 94.64



import math

def distance_between_points(p1, p2):
    return round(math.dist(p1, p2), 2)  # Uses formula

# Example usage
print(distance_between_points((1, 1), (4, 5)))     # Output: 5
print(distance_between_points((23, 17), (15, 27))) # Output: 12.81