# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(num1, num2):
  if num2 == 0:
    return "Division by zero is not allowed"
  else:
    return num1 / num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = div(num1, num2)
print("The division of", num1, "and", num2, "is:", result)

# 2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .
def square(num):
  return num * num
num = float(input("Enter a number: "))
result = square(num)
print("The square of", num, "is:", result)

# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
import numpy as np
np.random.seed(2)

numbers = [np.random.randint(1, 100) for _ in range(5)]

print("The numbers are:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

# 4. Accept a name from the user and display that in lower case using lower() function
name = input("Enter your name: ")
lower_name = name.lower()
print("Lowercase name:", lower_name)
