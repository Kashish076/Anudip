# 1. Python program to check leap year
year = int(input("Enter the year :"))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}, a leap year.")
else:
    print(f"{year}, not a leap year.")

# 2. Python Program to Find the Largest Among Three Numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
largest = max(num1, num2, num3)
print(f"Largest number is : {largest}")

# 3. Python Program to Check if a Number is Positive, Negative or 0
num = int(input("Enter a number:"))
if(num > 0):
    print(f"{num} is a positive number.")
elif(num < 0):
    print(f"{num} is a negative number.")
else:
    print(num)

# 4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500 Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
product_code = int(input("Enter product code (1 for Battery, 2 for Key, 3 for Electrical): "))
order_amount = float(input("Enter order amount: "))

discount = 0

if product_code == 1 and order_amount > 1000:
    discount = 0.1 * order_amount
elif product_code == 2 and order_amount > 100:
    discount = 0.05 * order_amount
elif product_code == 3 and order_amount > 500:
    discount = 0.1 * order_amount

net_amount = order_amount - discount

print("Discount:", discount)
print("Net amount:", net_amount)


# 5. A transport company charges the fare according to following table:
    # Distance Charges
    # 1-50 8 Rs./Km
    # 51-100 10 Rs./Km
    # > 100 12 Rs/Km
distance = float(input("Enter total distance travelled by transport:"))
if(distance >=1 and distance <= 50):
    charges = distance * 8
elif(distance >=51 and distance <= 100):
    charges = distance * 10
elif(distance > 100):
    charges = distance * 12
else:
    charges = 0
print("Total fare charge is : ",charges)

# 6. Write a python program to reverse a number using a while loop.
number = int(input("Enter the number to be reversed:"))
rev = 0
while(number>0):
    rem = number % 10
    rev = (rev*10)+rem
    number = number//10
print(f"Number after being reversed is {rev}")
    

# 7. Write a python program to check whether a number is palindrome or not?
value = int(input("Enter the number to be checked for palindrome:"))
original = value
rev = 0
while(original>0):
    rem = original % 10
    rev = (rev*10)+rem
    original = original//10
if(rev == value):
    print(f"{value} is a palindrome.")
else:
    print(f"{value} is not a palindrome.")

# 8. Write a python program finding the factorial of a given number using a while loop.
num = int (input("Enter a number for factorial :"))
n = num
fact = 1
while(n>0):
    fact = fact * n
    n -= 1
print(f"factorial of {num} is {fact}")

# 9. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
sum = 0
while True:
    x = int(input("Enter a number : "))
    sum += x
    if(x == 0):
        break    
print(f"The sum of numbers is {sum}")

# 10. Print the first 10 natural numbers using for loop
for i in range(1,11):
    print(i, end = ", " if i<10 else"\n")

# 11. Python program to check if the given string is a palindrome
string = input("Enter a string: ")
string = string.replace(" ", "").lower()
rev_string = string[::-1]

if string == rev_string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

# 12. Python program to check if a given number is an Armstrong number
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# 13. Python program to get the Fibonacci series between 0 to 50
def fib (n):
    if(n == 0 ):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
print("Fibonnaci series between 0 to 50: ")    
i = 0
while True:
    fib_number = fib(i)
    if fib_number > 50:
        break
    print(fib_number, end=", ")
    i += 1  

# 14. Python program to check the validity of password input by users
pswd = input("\nEnter your password:")
has_upper = False
has_lower = False
has_digit = False
has_special = False
for char in pswd:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in "@#$%^&+=":
        has_special = True
if(len(pswd)<8):
    print("Password must be atleast 8 letters.")
elif not has_upper:
    print("Password should contain at least one uppercase letter.")
elif not has_lower:
    print("Password should contain at least one lowercase letter.")
elif not has_digit:
    print("Password should contain at least one digit.")
elif not has_special:
    print("Password should contain at least one special character (@, #, $, etc.).")
else:
    print("Password is valid.")