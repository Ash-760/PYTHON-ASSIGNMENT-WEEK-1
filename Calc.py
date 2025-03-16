#prompt the user for the two numbers
num1 = float(input("Enter the first number: ")) 

num2 = float(input("Enter the first number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+": 
    print(num1, "+", num2, "=", num1 + num2)

elif operation == "-":
    print(num1, "-", num2, "=", num1 - num2)

elif operation == "*": 
    print(num1, "*", num2, "=", num1 * num2)

elif operation == "/": 
    if num2 == 0:  
        print("Error due to division by zero.")
    else:
        print(num1, "/", num2, "=", num1 / num2)

else:
    print("Invalid operation. Please enter +, -, *, or /") 