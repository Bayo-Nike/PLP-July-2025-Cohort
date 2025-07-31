# User Input
number1=input("Please Enter your first number:")
number2=input("Please Enter your second number:")
operation = input("Please enter your preferred mathematical operation (+, -, *, /): ").strip()

# Convert input strings to floats (you can use int if you prefer integer math)
num1 = float(number1)
num2 = float(number2)

def addition(num1,num2):
    return num1 + num2
def subtraction(num1,num2):
    return num1 - num2
def multiplication(num1,num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2

# Using match-case
match operation:
    case '+':
        result = addition(num1, num2)
    case '-':
        result = subtraction(num1, num2)
    case '*':
        result = multiplication(num1, num2)
    case '/':
        result = division(num1, num2)
    case _:
        result = "Invalid operation!"

print(f"Result: {result}")