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

- `Purpose`: Contains functions to convert infix expressions to postfix notation and evaluate them.
- `Features`:
   - Converts infix expressions to postfix notation.
   - Supports operators such as +, -, *, /, and ^ (for exponentiation).
   - Evaluates postfix expressions with proper operator precedence and associativity.
   - Error handling for invalid characters, mismatched parentheses, division by zero, and empty expressions.


2. **question2.py**

- `Purpose`: Expands on the functionality by adding custom error-handling and validation logic for complex expressions.
- `Features`:
   - Validates expressions to ensure they do not start with invalid operators.
   - Handles division by zero and mismatched parentheses.
   - Provides detailed feedback for various error cases, helping users identify issues in the input expression.


3. **question3.py**

- `Purpose`: Implements an interactive interface for users to input expressions and receive evaluation results or error messages.
- `Features`:
   - Accepts user input and evaluates the expression.
   - Outputs detailed results, including errors encountered during evaluation.
   - Designed to be user-friendly for both valid and invalid input expressions.

## Sample Input and Output

### Question 1 - Single Operator
| Input | Output |
|-------|--------|
| `2 + 5` | `7` |
| `8 - 3` | `5` |
| `5 * 4` | `20` |
| `8 / 2` | `4` |
| `4 ^ 2` | `16` |

### Question 2 - Multiple Operators and Parentheses
| Input         | Output |
|---------------|--------|
| `1 + 2 * 3`   | `7`    |
| `(1 + 2) * 3` | `9`    |
| `6 + 3 - 2 + 12` | `19` |
| `2 * 15 + 23` | `53`   |
| `10 - 3 ^ 2`  | `1`    |

### Question 3 - Decimal and Negative Numbers
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

   git clone https://github.com/vennamsandeep/calculator_project.git
   cd calculator_project

2. **Run the Code**:

   python questionX.py  
   
   ex: python question1.py

3. **Input Expressions**:

   When prompted, enter a valid infix expression to see the result. Each script will handle invalid cases and provide feedback.