# Better to separate the functions and have only 1 function per function

def double(num):
    str_num = str(num)
    length = len(str_num)
    mid_index = length // 2
    return str_num[:mid_index] == str_num[mid_index:]

def twice(num):
    if double(num):
        return num
    else:
        return num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True