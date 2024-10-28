'''
Question 1
Solve simple expressions with a single operator and two operands. All binary operations are
permissible (addition, subtraction, multiplication, division and exponentiation).
Acceptable input
• Single operator: + - * / ^
• Positive integers
• White space (should be ignored)
• Error Handling
'''



import re

def evaluate_expression(expression):
    # Remove whitespace from the expression
    expression = expression.replace(" ", "")
    
    # Define operation functions using lambdas
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",  # Handle division by zero
        '^': lambda x, y: x ** y
    }
    
    # Validate the expression format
    if not re.match(r"^\d+\s*[\+\-\*/\^]\s*\d+$", expression):
        return "Invalid input. Please enter a valid expression."
    
    # Identify the operator and split the operands
    for i, c in enumerate(expression):
        if c in operations:
            try:
                left = int(expression[:i])
                right = int(expression[i+1:])
                operator = c
                break
            except ValueError:
                return "Invalid input. Operands should be positive integers."
    
    # Perform the calculation
    result = operations[operator](left, right)
    return result

if __name__ == "__main__":
    print("welcome to the simple Calulator! Please enter a simple expression you want to evaluate.")
    print("Type quit to exit")
    while True:
        expression=input("Enter the expression:")
        if expression == "quit":
            break
        else:
            print(evaluate_expression(expression))
    