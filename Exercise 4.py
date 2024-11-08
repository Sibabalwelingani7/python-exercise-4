# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "banana", "grape", "strawberry"]
for fruit in fruits:
# TODO: Use a for loop to print each fruit in the list
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count >= 1:
    print(count)
    count -=1
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for num in range (1,11):
    square = num ** 2
    print(square)
#--------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ["pink", "blue", "yellow", "green" ]
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):  
    random_color = random.choice(colors) 
    print(random_color) 

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
    else:
        print("invalid choice, please try again")
# TODO: Import the custom module and use its functions
while true:
   if operation == "+":
        print (a+b)
        result = a + b
   elif operation == "-":
        print (a-b)
        result = a - b
   elif operation == "*":
       print (a*b)
       result = a * b
   elif b != 0 and operation == "/":
        print (a / b)
   else:
    print("Error: Division by zero")               

# TODO: Use a while loop to create a simple calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero."