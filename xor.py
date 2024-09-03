def xor(first, second):
    return (bool(first) + bool(second)) == 1

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

# This one is elegant:

# def xor(arg1, arg2):
#     return bool(arg1) != bool(arg2)