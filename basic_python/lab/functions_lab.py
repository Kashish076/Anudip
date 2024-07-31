# ASSIGNMENT 1
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
print("-----------------------------------------------------")

# 2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .
def square(num):
  return num * num
num = float(input("Enter a number: "))
result = square(num)
print("The square of", num, "is:", result)
print("-----------------------------------------------------")

# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
import numpy as np
np.random.seed(2)
numbers = [np.random.randint(1, 100) for _ in range(5)]
print("The numbers are:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("-----------------------------------------------------")

# 4. Accept a name from the user and display that in lower case using lower() function
name = input("Enter your name: ")
lower_name = name.lower()
print("Lowercase name:", lower_name)
print("-----------------------------------------------------")

# ASSIGNMENT 2
# 1. Write a Python program to count the occurrences of each word in a given sentence
# string = “To change the overall look of your document. To change the look available in the gallery”
string = "To change the overall look of your document. To change the look available in the gallery"
words = string.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"{word}: {count}")
print("-----------------------------------------------------")
    

# 2. Write a Python program to remove a newline in Python
# String = "\nBest \nDeeptech \nPython \nTraining\n"
string = "\nBest \nDeeptech \nPython \nTraining\n"
string = string.strip()
string = string.replace("\n", "")
print(string)
print("-----------------------------------------------------")

# 3. Write a Python program to reverse words in a string
# String = “Deeptech Python Training”
string = "Deeptech Python Training"
words = string.split()
reversed_words = words[::-1]
reversed_string = " ".join(reversed_words)
print(reversed_string)
print("-----------------------------------------------------")

# 4. Write a Python program to count and display the vowels of a given text
# String=”Welcome to python Training”
string = "Welcome to python Training"
string = string.lower()
vowels = "aeiou"
count = 0
for char in string:
  if char in vowels:
    count += 1
print("Number of vowels:", count)
print("-----------------------------------------------------")

# ASSIGNMENT 3
#1. Write a Python program to Count all letters, digits, and special symbols from the given string
# Input = “P@#yn26at^&i5ve”
# Output: Chars = 8 Digits = 2 Symbol = 3
string = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0
for char in string:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)
print("-----------------------------------------------------")


# 2. Write a Python program to remove duplicate words of a given string.
# Input = “String and String Function”
# Output: String and Function
def remove_duplicate_words(string):
  words = string.split()
  unique_words = []
  for word in words:
    if word not in unique_words:
      unique_words.append(word)
  return " ".join(unique_words)
string = "String and String Function"
output = remove_duplicate_words(string)
print(output)
print("-----------------------------------------------------")


# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
# Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
# Output:
    # UpperCase : 5
    # LowerCase : 18
    # NumberCase : 5
    # SpecialCase : 11
def count_chars(string):
  uppercase = 0
  lowercase = 0
  digits = 0
  special_chars = 0
  for char in string:
    if char.isupper():
      uppercase += 1
    elif char.islower():
      lowercase += 1
    elif char.isdigit():
      digits += 1
    else:
      special_chars += 1
  return uppercase, lowercase, digits, special_chars
string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase, lowercase, digits, special_chars = count_chars(string)
print("UpperCase :", uppercase)
print("LowerCase :", lowercase)
print("NumberCase :", digits)
print("SpecialCase :", special_chars)
print("-----------------------------------------------------")


# 4. Write a Python Count vowels in a string
# input= “Welcome to Python Assignment”
# Output: Total vowels are: 8
def count_vowels(string):
  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count

string = "Welcome to Python Assignment"
vowel_count = count_vowels(string)
print("Total vowels are:", vowel_count)
