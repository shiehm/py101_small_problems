# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. 
# The UTF-16 string value is the sum of the UTF-16 values of every character in the string. 
# (You may use ord to determine the UTF-16 value of a character.)

# 1. Pass a string to the function
# 2. Iterate through each character
# 3. Determine the UTF value of each character 
# 4. Add that value to the cumulative total 
# 5. Return the total 

def utf16_value(string):
    total = 0
    for char in string:
        value = ord(char)
        total += value
    return total 

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)