# Author: Rickard Andersson

# Syntax in cli: python3 calc.py 

var_number1 = float(input("Enter a number greater than 1: "))
var_number2 = float(input("Enter a number greater than 1: "))
oper = input("Choose a math operation (+, -, *, /): ")
while True:
    if oper == '+':
        print(var_number1, oper, var_number2, '=', var_number1 + var_number2)
        break
    elif oper == '-':
        print(var_number1, oper, var_number2, '=', var_number1 - var_number2)
        break
    elif oper == '*':
        print(var_number1, oper, var_number2, '=', var_number1 * var_number2)
        break
    elif oper == '/':
        print(var_number1, oper, var_number2, '=', var_number1 / var_number2)
        break
    else:
        print('operator is not supported')
        break
