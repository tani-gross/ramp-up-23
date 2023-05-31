import math

def circle_or_square(radius, side_length):
    circumference = 2 * math.pi * radius
    perimeter = 4 * side_length

    return circumference > side_length