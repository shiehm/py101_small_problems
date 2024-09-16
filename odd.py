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
    
    if end_num % 2 == 0:
        end_num += 1
    
    for i in range(start_num, end_num, 2):
        print(i)

print_odds()