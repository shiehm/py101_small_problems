# Write a function that takes one integer argument and 
# returns True when the number's absolute value is odd, False otherwise.

def is_it_odd(num):
    return abs(int(num)) % 2 != 0
    
# for num in range(-10, 11):
#     print(num, is_it_odd(num))
    

# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

def print_odds():
    start_num = int(input('Choose a starting odd integer: '))
    end_num = int(input('Choose an ending odd integer: '))
    
    while end_num < start_num:
        end_num = int(input('Ending integer must be greater than starting integer: '))
    
    if start_num % 2 == 0:
        start_num += 1
    
    if end_num % 2 ==0:
        end_num += 1
    
    for i in range(start_num, end_num, 2):
        print(i)


# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# Modify the program to let the user specify the measurement type (meters or feet). 
# Compute the area accordingly and print it and its conversion in parentheses.

SQ_METER_IN_FT = 10.7639 # 1 sq meter = 10.7639 sq ft

def room_size():
    
    units = input('Do you want to use feet or meters? (type feet or meters): ').lower()
    
    while not (units.startswith('f') or units.startswith('m')):
        units = input('Invalid selection, please type feet or meters: ')
    
    width = float(input(f'What is the width in {units}? ')) 
    length = float(input(f'What is the length in {units}? ')) 
    
    if units.startswith('m'):
        area_in_meters = width * length
        area_in_feet = area_in_meters * SQ_METER_IN_FT
        
        print(f'The size of the room is {area_in_meters:.2f} sq meters.')
        print(f'The size of the room is {area_in_feet:.2f} sq feet.')

    elif units.startswith('f'):
        area_in_feet = width * length
        area_in_meters = area_in_feet / SQ_METER_IN_FT
        
        print(f'The size of the room is {area_in_feet:.2f} sq feet.')
        print(f'The size of the room is {area_in_meters:.2f} sq meters.')


def tip_calc():
    bill = float(input('What is the bill? '))
    tip_pct = float(input('What is the tip percentage? '))
    tip_amt = tip_pct/100 * bill
    bill_amt = tip_amt + bill
    
    print(f'The tip is ${tip_amt:.2f}')
    print(f'The total is ${bill_amt:.2f}')
    

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