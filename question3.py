'''
Question 3
Expressions may now also contain non-integer numbers, as well as negative numbers and 0.
Acceptable input
• One or more operators: + - * / ^
• Parentheses: ( )
• Integers and decimal numbers
• White space (should be ignored)
• Error Handling
'''



import re

#helper functions to evaluate the code
            
#check to see if the token is a operator. 
def is_operator(token):
    return token in "+-*/^"

#function to convert the expression into tokens
def tokenize(expression):
    # Remove all whitespaces
    expression = expression.replace(" ", "")
    
    tokens = re.findall(r'\d*\.\d+|\d+|[+*/^()-]', expression)
    
    if not tokens:
        raise ValueError("Empty input is not a valid expression.")
    
    return tokens

#function to check if the given expression is valid
def is_valid_expression(expression):
    if not re.match(r"^\s*[\d+\-*/^()\s]+\s*$", expression):
        return False
    return True

def infix_to_postfix(expression):
    # Clean and validate the expression
    expression = expression.replace(" ", "")
    if not re.match(r'^[\d+\-*/^().]*$', expression):
        raise ValueError("Expression contains invalid characters.")
    
    # Tokenize the input, allowing for decimals, parentheses, and unary minus
    tokens = re.findall(r'\d*\.\d+|\d+|[+*/^()-]', expression)
    if not tokens:
        raise ValueError("Empty input is not a valid expression.")
    
    output, operators = [], []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    for i, token in enumerate(tokens):
        # Handle unary minus by merging '-' with the next token if needed
        if token == '-' and (i == 0 or tokens[i - 1] in "()+-*/^"):
            tokens[i + 1] = '-' + tokens[i + 1]  # Merge '-' with the next number
            continue
        
        # Process tokens based on their type
        if re.match(r'-?\d+(\.\d+)?', token):  # Numbers (integers or decimals)
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if not operators:
                raise ValueError("Mismatched parentheses.")
            operators.pop()  # Remove '('
        elif token in precedence:
            while operators and operators[-1] != '(' and precedence[operators[-1]] >= precedence[token]:
                output.append(operators.pop())
            operators.append(token)
    
    # Pop all remaining operators from the stack
    while operators:
        op = operators.pop()
        if op in '()':
            raise ValueError("Mismatched parentheses.")
        output.append(op)
    
    return output


def evaluate_postfix(postfix):
    
    operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",  # Handle division by zero
    '^': lambda x, y: x ** y
    }

    stack = []
    
    for token in postfix:
        if re.match(r'-?\d+(\.\d+)?', token):  # Token is a number (integer or decimal)
            stack.append(float(token))
        elif token in "+-*/^":
            if len(stack) < 2:
                raise ValueError("Invalid expression format: insufficient operands.")
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operations[token](operand1, operand2)
            stack.append(result)
    
    if len(stack) != 1:
        raise ValueError("Invalid expression format.")
    
    return stack[0]


def main():
    expression = input("Enter a valid infix expression: ")

    try:
        # Convert infix to postfix
        postfix = infix_to_postfix(expression)
        #print("Postfix notation:", ' '.join(postfix))
        
        # Evaluate the postfix expression
        result = evaluate_postfix(postfix)
        print("Result:", result)

    except ZeroDivisionError as e:
        print("Error:", e)
    except ValueError as e:
        print("Input Error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    print("Please enter the expression you want to evaluate.")
    main()

    