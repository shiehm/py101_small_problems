# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product 
# of all numbers between 1 and the entered integer, inclusive.

def sum_or_product():
    num = int(input('Please enter an integer great than 0: '))
    while num < 1:
        print('Invalid choice.')
        num = int(input('Please enter an integer great than 0: '))
    
    operator = input('Please enter "s" for sum or "p" for product: ')
    while not (operator.startswith('s') or operator.startswith('p')):
        print('Invalid choice.')
        operator = input('Please enter "s" for sum or "p" for product: ')
    
    total = 1
    for i in range(2, num + 1):
        if operator == 's':
            total += i
        elif operator == 'p':
            total *= i
    
    print(f'The total of the operation on consecutive integers 1-{num} is: {total}')

# You can sum ranges directly, you can perform operations:
# This solution is pythonically better because it keeps each operation separate (sum or product)
# It's modular, you have just one function for the function
# It defines the separate functions first, then does the input and conditional output operations

# def compute_sum(target_num):
#     return sum(range(1, target_num+1))

# def compute_product(target_num):
#     result = 1
#     for num in range(1, target_num+1):
#         result *= num
#     return result

# prompt1 = "Please enter an integer greater than 0: "
# prompt2 = ('Enter "s" to compute the sum, '
#           'or "p" to compute the product: ')

# number = int(input(prompt1))
# operation = input(prompt2)
# print()

# if operation == "s":
#     print("The sum of the integers between 1 and "
#           f"{number} is {compute_sum(number)}.")
# elif operation == "p":
#     print("The product of the integers between 1 and "
#           f"{number} is {compute_product(number)}.")
# else:
#     print("Oops. Unknown operation.")

# Suppose the input was a list of space separated integers instead of just a single integer? 
# How would your compute_sum and compute_product functions change?