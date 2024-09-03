# Pass in a string 
# If there are any consecutive duplicate characters, compress them 

def crunch(string):
    crunched_str = ''
    prior = ''
    for char in string:
        if char != prior:
            crunched_str += char
        prior = char
    return crunched_str

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')