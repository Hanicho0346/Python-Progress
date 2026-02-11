 

# question 4:Simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 !=0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation. Please choose from +, -, *, /."


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

result = calculator(num1, num2, operation)
print(f"The result is: {result}")