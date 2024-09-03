# First figure out if it is an odd or even length string
# If odd, return the middle character (len(string)//2)
# If even, return the middle 2 characters (len(string)/2 and -1)

def center_of(string):
    length = len(string)
    mid = length // 2
    if length % 2 != 0:
        return string[mid]
    else:
        return string[mid - 1:mid + 1]

print(center_of('I Love Python!!!'))    # True
print(center_of('Launch School'))        # True
print(center_of('Launchschool'))        # True
print(center_of('Launch'))              # True
print(center_of('Launch School is #1'))  # True
print(center_of('x'))                    # True

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True