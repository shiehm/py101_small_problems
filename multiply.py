def multiply(num1, num2):
    return num1 * num2

print(multiply(5, 3))
print(multiply(5, 3) == 15)  # True

def square(num):
    return multiply(num, num)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True


# Suppose we want to generalize this function to a "power to the n" type function: 
# cubed, to the 4th power, to the 5th, etc. How would we go about doing so while still using the multiply function?

def power_of_n(num, power):
    result = 1
    for i in range(power):
        result = multiply(result, num)
    return result
    
power_of_n(5,5)