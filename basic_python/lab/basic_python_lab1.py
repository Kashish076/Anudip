# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
num = int(input("Enter a Number:"))
result = ("Even" if(num%2==0) else "False")
print(f"The number is {result}")
print("--------------------------------------------------------------------")

# 2. Using input function take two number and then swap the number
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(f"Numbers before swapping : first number is {num1} and second number is {num2}")
num1,num2 = num2,num1
print(f"Numbers after swapping : first number is {num1} and second number is {num2}")
print("--------------------------------------------------------------------")

# 3. Write a Program to Convert Kilometers to Miles
KM = float(input("Enter distance in Kilometers: "))
miles = KM * 0.621371
print(f"{KM} kilometers is equal to {miles} miles.")
print("--------------------------------------------------------------------")

# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year

Amount = 200  
Rate = 5    
Time = 5  
simple_interest = (Amount * Rate * Time) / 100
print(f"The simple interest on Rs. {Amount} for {Time} years at {Rate}% per year is Rs. {simple_interest}.")
