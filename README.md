# Calculator Application

This project is a calculator application that solves various types of mathematical expressions without using any built-in evaluation functions like `eval`. It is implemented in Python with multiple functions to handle different levels of expression complexity, including support for multiple operators(+ . - , / , * , ^ ), parentheses, integer and decimal values, and negative numbers.

## Features

The application can handle:
1. **Single operator with two operands** (addition, subtraction, multiplication, division, exponentiation).
2. **Multiple operators with proper precedence** (addition, subtraction, multiplication, division, exponentiation) and parentheses.
3. **Expressions with decimal numbers, negative numbers, and parentheses**.

Each question has been solved in a separate file:
- `question1.py`: Single operator expressions
- `question2.py`: Multiple operators with parentheses and precedence
- `question3.py`: Multiple operators with parentheses, decimal numbers, and negative numbers

## Files and Descriptions
1. **question1.py**

**Features**
- Basic operations like +, -, *, /, ^.
- Error handling for division by zero.
- Validation to ensure only simple two-operand expressions are processed.


2. **question2.py**

**Features**
- Handles expressions with multiple operators and parentheses.
- Supports integers only.
- Infix to postfix conversion for more complex evaluation.
- Operator precedence and associativity are correctly implemented.
- Error handling for invalid expressions and mismatched parentheses.


3. **question3.py**

- Supports both integer and floating-point numbers.
- Handles unary minus for expressions like -3 + 2.
- Infix to postfix conversion and subsequent evaluation.
- Proper error handling for invalid characters, insufficient operands, and division by zero.
- Checks for mismatched parentheses.

## Sample Input and Output

### Question 1 - Single Operator
- question.py: Enter simple expressions like 5 + 3 or 10 * 4. Type quit to exit.

| Input | Output |
|-------|--------|
| `2 + 5` | `7` |
| `8 - 3` | `5` |
| `5 * 4` | `20` |
| `8 / 2` | `4` |
| `4 ^ 2` | `16` |

### Question 2 - Multiple Operators and Parentheses
- question2.py: Enter more complex infix expressions such as (3 + 5) * 2 or 4 / (2 + 3).

| Input         | Output |
|---------------|--------|
| `1 + 2 * 3`   | `7`    |
| `(1 + 2) * 3` | `9`    |
| `6 + 3 - 2 + 12` | `19` |
| `2 * 15 + 23` | `53`   |
| `10 - 3 ^ 2`  | `1`    |

### Question 3 - Decimal and Negative Numbers
question3.py: Enter complex infix expressions including negative and floating numbers such as (-20 * 1.8) / 2 or -53 + -24.

| Input                | Output   |
|----------------------|----------|
| `3.5 * 3`            | `10.5`   |
| `-53 + -24`          | `-77`    |
| `10 / 3`             | `3.333`  |
| `(-20 * 1.8) / 2`    | `-18`    |
| `-12.315 - 42`       | `-54.315`|

## Prerequisites

- Python 3.x installed on your local machine

## Running the Application

To test each question, you can run the respective Python file from the command line.

### Steps:
1. **Clone the repository**:

   ```git clone https://github.com/vennamsandeep/calculator_project.git```

   ```cd calculator_project```

2. **Run the Code**:

   ```python questionX.py```
   
   ```ex: python question1.py```

3. **Input Expressions**:

   When prompted, enter a valid infix expression to see the result. Each script will handle invalid cases and provide feedback.