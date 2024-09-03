def print_box(string):
    length = len(string)
    print('+-' + '-' * length + '-+')
    print('| ' + ' ' * length + ' |')
    print('| ' + string + ' |')
    print('| ' + ' ' * length + ' |')
    print('+-' + '-' * length + '-+')
    
print_box('hello')