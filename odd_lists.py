def oddities(full_list):
    odd_list = []
    for i in range(len(full_list)):
        if i % 2 == 0:
            odd_list.append(full_list[i])
    return odd_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

# Slicing makes it easier, it's like range where you can add the step
# def oddities(lst):
#     return lst[::2]