def clean_up(string):
    cleaned_string = ''
    prior = ''
    for char in string:
        if char.isalpha():
            cleaned_string += char
        elif prior.isalpha() or prior == '':
            cleaned_string += ' '

        prior = char
    return cleaned_string

print(clean_up("---what's my +*& line?"))
print(clean_up("---what's my +*& line?") == " what s my line ")