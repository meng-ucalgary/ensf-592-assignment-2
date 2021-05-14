# calculator.py
# BHAVYAI GUPTA
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 2 git repository.
#


# tuple to hold the valid arithmetic operators
valid_operators = ("+", "-", "*", "/")


# function to print all the valid arithmetic operators
# parameters - none
# returns - None
def print_valid_operators():
    for op in valid_operators:
        print(op, end='')
    print()


# function to check validity of input operator
# parameters - string holding the operator
# returns - True if the parameter is valid, otherwise False
def check_operator_validity(o):
    if o in valid_operators:
        return True
    else:
        return False


# function to compare precendence of first arithmetic operator with the second arithmetic operator
# parameters - two string, each holding the arithmetic operator
# returns - True if first arithmetic operator has higher precedence over the second arithmetic operator, False otherwise
def compare_operator_precedence(o1, o2):
    index_o1 = valid_operators.index(o1)
    index_o2 = valid_operators.index(o2)

    if(index_o1 > index_o2):
        return True
    else:
        return False


# function to evaluate a basic arithmetic operation between two integers
# parameters - integer operand 1, arithmetic operator in string, integer operand 2
# returns - evaluated result of the two integer parameters in float
def operation(a, o, b):
    if(o == valid_operators[0]):
        return float(a + b)
    elif(o == valid_operators[1]):
        return float(a - b)
    elif(o == valid_operators[2]):
        return float(a * b)
    else:
        return float(a / b)


# function to evaluate an arithmetic expression which is formed by series of user input
# follow DMAS rule during evaluation
# parameters - integer operand, string containing operator, integer operand, string containing operator, integer operand
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

# ask the user for input of first integer, and convert the string to int
x = int(input("Please enter first integer operand: "))

while True:
    o1 = input("Please enter the first operator: ")

    # check if the operand entered by user in valid
    if check_operator_validity(o1):
        break
    else:
        print("[FAIL] Invalid operator entered, only supported operators are ", end='')
        # print all the valid arithmetic operators to alert the user in case of bad input
        print_valid_operators()

# ask the user for input of second integer, and convert the string to int
y = int(input("Please enter second integer operand: "))

while True:
    o2 = input("Please enter the second operator: ")

    # check if the operand entered by user in valid
    if check_operator_validity(o2):
        break
    else:
        print("[FAIL] Invalid operator entered, only supported operators are ", end='')
        # print all the valid arithmetic operators to alert the user in case of bad input
        print_valid_operators()

# ask the user for input of third integer, and convert the string to int
z = int(input("Please enter third integer operand: "))


# print the arithmetic expression and the result
print("Result for the expression", x, o1, y, o2, z, ":", evaluate_expression(x, o1, y, o2, z))

