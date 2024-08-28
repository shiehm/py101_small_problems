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