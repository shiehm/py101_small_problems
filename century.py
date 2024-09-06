def century(year):
    if year % 100 == 0:
        century_num = str(year // 100)
    else:
        century_num = str((year // 100) + 1)
    
    if len(century_num) > 1 and century_num[-2] == '1':
        century_end = 'th'
    elif century_num[-1] == '1':
        century_end = 'st'
    elif century_num[-1] == '2':
        century_end = 'nd'
    elif century_num[-1] == '3':
        century_end = 'rd'
    else:
        century_end = 'th'
    
    century = str(century_num) + century_end
    return century

print(century(2000))
print(century(2001))
print(century(1965))
print(century(256))
print(century(5))
print(century(10103))
print(century(1052))
print(century(1127))
print(century(11201))

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True