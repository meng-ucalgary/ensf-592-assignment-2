# calculator.py
# BHAVYAI GUPTA
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 2 git repository.
#


# tuple to hold the valid arithmetic operators
valid_operators = ("+", "-", "*", "/")


# function to print all the valid arithmetic operators
# arguments - none
# returns - None
def print_valid_operators():
    for op in valid_operators:                  # loop through the tuple which holds the valid arithmetic operators
        # print the valid operators without the default newline
        print(op, end='')
    print()                                     # empty print to print a newline


# function to check the validity of input operator
# arguments - string holding the operator
# returns - True if the parameter is valid, otherwise False
def check_operator_validity(o):
    if o in valid_operators:                    # check if the string argument is in the tuple valid_operators
        return True
    else:
        return False


# function to compare precendence of first arithmetic operator with the second arithmetic operator
# arguments - two string, each holding the arithmetic operator
# returns - True if first arithmetic operator has higher precedence over the second arithmetic operator, False otherwise
def compare_operator_precedence(o1, o2):
    index_o1 = valid_operators.index(o1)
    index_o2 = valid_operators.index(o2)

    if(index_o1 > index_o2):                    # compare the index of the operators in the tuple
        return True
    else:
        return False


# function to evaluate a basic arithmetic operation between two integers
# arguments - integer operand 1, arithmetic operator in string, integer operand 2
# returns - evaluated result of the two integer arguments in float
def operation(a, o, b):
    if(o == valid_operators[0]):
        return float(a + b)
    elif(o == valid_operators[1]):
        return float(a - b)
    elif(o == valid_operators[2]):
        return float(a * b)
    else:
        return float(a / b)


# function to evaluate an arithmetic expression which is formed by user inputs
# arguments - integer operand 1, string containing operator 1, integer operand 2, string containing operator 2, integer operand 3
# returns - evaluated result of the arithmetic expression in float
def evaluate_expression(a, op1, b, op2, c):
    if(compare_operator_precedence(op1, op2)):
        result = operation(a, op1, b)
        return operation(result, op2, c)

    else:
        result = operation(b, op2, c)
        return operation(a, op1, result)


# print the welcome message
print("\n\nWelcome to 3-operand-and-2-operator Calculator\n\n")

# ask the user for input of first integer, and convert the entered string to int
x = int(input("Please enter first integer operand: "))


# loop infinitely until user enters the correct arithmetic operator
while True:
    o1 = input("Please enter the first operator: ")

    # check if the operand entered by user in valid, if not alert the user
    if check_operator_validity(o1):
        break
    else:
        print("[FAIL] Invalid operator entered, only supported operators are ", end='')
        print_valid_operators()


# ask the user for input of second integer, and convert the entered string to int
y = int(input("Please enter second integer operand: "))


# loop infinitely until user enters the correct arithmetic operator
while True:
    o2 = input("Please enter the second operator: ")

    # check if the operand entered by user in valid, , if not alert the user
    if check_operator_validity(o2):
        break
    else:
        print("[FAIL] Invalid operator entered, only supported operators are ", end='')
        print_valid_operators()


# ask the user for input of third integer, and convert the entered string to int
z = int(input("Please enter third integer operand: "))


# print the arithmetic expression and the result
print("Result for the expression", x, o1, y, o2, z, ":", evaluate_expression(x, o1, y, o2, z))
