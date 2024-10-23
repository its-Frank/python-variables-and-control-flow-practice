#Write a Python program that takes the lengths of three sides of a triangle as input and determines if the triangle is equilateral, isocles, scalene
# Function to determine the type of triangle
def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input! Side lengths must be positive."
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Take user input for the lengths of the sides
try:
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Determine and print the type of triangle
    result = triangle_type(side1, side2, side3)
    print("The triangle is:", result)
except ValueError:
    print("Error: Please enter valid numbers for the side lengths.")
