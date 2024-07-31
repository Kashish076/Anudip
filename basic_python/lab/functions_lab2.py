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

