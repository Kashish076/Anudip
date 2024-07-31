# ASSIGNMENT (List)
# 1. Write a Python program to sum all the items in a list.
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print("The sum of all the items in the list is:", total_sum)
print("-----------------------------------------------------")


# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.
numbers = [34, 7, 23, 32, 5, 62, 14]
if numbers:
    min_num = max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    print("The smallest number in the list is:", min_num)
    print("The largest number in the list is:", max_num)
else:
    print("The list is empty.")
print("-----------------------------------------------------")


# 3. Write a Python program to find duplicate values from a list and display those.
numbers = [1, 3, 2, 4, 3, 5, 2, 6, 7, 1, 8]
duplicates = []
for i in range(len(numbers)):
    if numbers[i] not in duplicates:
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
                break
if duplicates:
    print("Duplicate values in the list are:", duplicates)
else:
    print("No duplicates found.")
print("-----------------------------------------------------")


# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3
first_part = original_list[:length_of_first_part]
second_part = original_list[length_of_first_part:]
print("Original list:")
print(original_list)
print("Length of the first part of the list:", length_of_first_part)
print("Splitted the said list into two parts:",first_part,second_part)
print("-----------------------------------------------------")

# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
original_list = ['red', 'green', 'white', 'black']
print("Traverse the said list in reverse order:")
for index in range(len(original_list) - 1, -1, -1):
    print(original_list[index])
print("-----------------------------------------------------")    
        
# ASSIGNMENT(Dictionary)
# 1. Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean_value = sum(test_dict.values()) / len(test_dict)
print("Mean of the dictionary values:", mean_value)
print("-----------------------------------------------------")

# 2.Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result_dict = {}
result_dict.update(dic1)
result_dict.update(dic2)
result_dict.update(dic3)
print("Concatenated dictionary :", result_dict)
print("-----------------------------------------------------")


# 3.Write a Python program to get the key, value and item in a dictionary.
# input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Key\tValue")
for key, value in dict_num.items():
    print(f"{key}\t{value}")
print("-----------------------------------------------------")


# 4.Write a Python program to get the key, value and item in a dictionary.
# Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
cleaned_dict = {key: value for key, value in input_dict.items() if value is not None}
print("dict with empty items Dropped :")
print(cleaned_dict)
print("-----------------------------------------------------")

# ASSIGNMENT(Tuples)
# 1. Write a Python program to find the number of times 4 appears in the tuple.
# Input:
# tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
value_to_count = 4
count = tuplex.count(value_to_count)
print(f"The number {value_to_count} appears {count} times in the tuple.")
print("-----------------------------------------------------")


# 2.Write a Python program to convert a list to a tuple.
# Input: listx = [5, 10, 7, 4, 15, 3]
listx = [5, 10, 7, 4, 15, 3]
tup = tuple(listx)
print("Converted tuple:", tup)
print("-----------------------------------------------------")


# 3. Write a Python program to calculate the sum of the numbers in a given tuple.
# Input: tuples_list = [(1, 2), (3, 4), (5, 6)]
tuples_list = [(1, 2), (3, 4), (5, 6)]
total_sum = sum(sum(tup) for tup in tuples_list)
print("Sum of tuple is:", total_sum)
print("-----------------------------------------------------")


# 4.Write a python program and iterate the given tuples
# Input:
# employee1 = ("John Doe", 101, "Human Resources", 60000)
# employee2 = ("Alice Smith", 102, "Marketing", 55000)
# employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employees = [employee1, employee2, employee3]
print("Employee Records :")
for employee in employees:
    name, emp_id, department, salary = employee
    print(f"Name : {name}")
    print(f"Employee ID : {emp_id}")
    print(f"Department : {department}")
    print(f"Salary : {salary}")
    print()
print("-----------------------------------------------------")

# ASSIGNMENT(Sets)
# 1. Write a Python program to Get Only unique items from two sets.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = set1 | set2
print("Unique items from both sets:", unique_items)
print("-----------------------------------------------------")


# 2. Write a Python program to Return a set of elements present in Set A or B, but not both.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_elements = set1 ^ set2
print("Elements present in Set A or B, but not both:", unique_elements)
print("-----------------------------------------------------")


# 3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
common_elements = set1 & set2
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements.")
print("-----------------------------------------------------")


# 4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
common_elements = set1 & set2
set1.intersection_update(set2)
print( set1)

