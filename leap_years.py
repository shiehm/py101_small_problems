# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year. <-- noise
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

def is_leap_year(year):
    if int(year) < int(1752):
        return year in range (1752, -1, -4)
    else:
        return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)