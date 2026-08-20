import math

# Ask the user to enter the length of side a
a = float(input("Enter the length of side a: "))

# Ask the user to enter the length of side b
b = float(input("Enter the length of side b: "))

# Use pow() to square the values of a and b
a_squared = math.pow(a, 2)
b_squared = math.pow(b, 2)

# Add the two squared values
sum_of_squares = a_squared + b_squared

# Use sqrt() to calculate the hypotenuse
hypotenuse = math.sqrt(sum_of_squares)

# Display the hypotenuse rounded to two decimal places
print(f"The hypotenuse is: {hypotenuse:.2f}")
