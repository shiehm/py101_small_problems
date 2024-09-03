# Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

def greet(name):
    name = input('Enter your name: ')
    if name.endswith('!'):
        print(f'HELLO {name} WHY ARE WE YELLING?'.upper())
    else:
        print(f'Hello {name}.')
        
greet()