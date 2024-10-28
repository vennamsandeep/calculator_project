'''
Question 2
Solve expressions with multiple operators. Expressions may now also contain parentheses, which
have a higher precedence level than the other operators.
Acceptable input
• One or more operators: + - * / ^
• Parentheses: ( )
• Positive integers
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
    
    tokens = re.findall(r'\d+|[+*/^()-]', expression)
    
    if not tokens:
        raise ValueError("Empty input is not a valid expression.")
    
    return tokens

#function to check if the given expression is valid
def is_valid_expression(expression):
    if not re.match(r"^\s*[\d+\-*/^()\s]+\s*$", expression):
        return False
    return True

def infix_to_postfix(expression):
    
    #with multiple levels of operators, we have setup a precedence to the operators.
    precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}

    # Check if the expression has invalid characters
    if not is_valid_expression(expression):
        return "Invalid input. Please enter a valid expression."
    
    # Tokenize the input for multiple operators and operands, allowing parentheses
    tokens = tokenize(expression)
    
    output = []  # Output list for postfix
    operators = []  # Stack for operators
    last_token = None
    
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if not operators:
                raise ValueError("Mismatched parentheses.")
            operators.pop()  # Remove '('
        elif is_operator(token):
            # Adjusted check to avoid raising an error on valid expressions
            if last_token is None or last_token == '(':
                raise ValueError(f"Invalid position for operator '{token}' at the start of expression.")
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)
        else:
            raise ValueError(f"Invalid character found: {token}")
        
        last_token = token
    
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
        if token.isdigit():
            stack.append(int(token))
        elif is_operator(token):
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