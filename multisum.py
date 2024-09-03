# Write a function that computes the sum of all numbers 
# between 1 and some other number, inclusive, that are multiples of 3 or 5.
# You may assume that the number passed in is an integer greater than 1.

# Find the multiples of 3 from 1 to that number 
# Find the multiples of 5 from 1 to that number 

def multisum(num):
    multi_3 = set(range(0, num + 1, 3))
    multi_5 = set(range(0, num + 1, 5))
    multi_set = multi_3.union(multi_5)
    return sum(multi_set)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

print(multisum(3))
print(multisum(5))
print(multisum(10))
print(multisum(1000))