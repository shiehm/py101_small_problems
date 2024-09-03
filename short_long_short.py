def short_long_short(str1, str2):
    if len(str1) < len(str2):
        return str1 + str2 + str1
    else:
        return str2 + str1 + str2
    
# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

print(short_long_short('abc', 'defgh'))
print(short_long_short('abcde', 'fgh'))
print(short_long_short('', 'xyz'))