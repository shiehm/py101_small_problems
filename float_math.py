# Write a program that prompts the user for two positive numbers (floating-point), 
# then prints the results of the following operations on those two numbers: 
# addition, subtraction, product, quotient, floor quotient, remainder, and power. 
# Do not worry about validating the input.

def float_math():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} - {num2} = {num1 - num2}')
    print(f'{num1} * {num2} = {num1 * num2}')
    print(f'{num1} / {num2} = {num1 / num2}')
    print(f'{num1} // {num2} = {num1 // num2}')
    print(f'{num1} % {num2} = {num1 % num2}')
    print(f'{num1} ** {num2} = {num1 ** num2}')

float_math()