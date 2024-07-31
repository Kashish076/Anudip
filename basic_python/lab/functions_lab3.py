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
