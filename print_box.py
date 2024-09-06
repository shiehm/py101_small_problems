def print_box(string, max_len=20):
    length = len(string)    
    trunc = (length // max_len) + 1
    end_spaces = max_len - (length % max_len)
    
    print('+-' + '-' * max_len + '-+')
    print('| ' + ' ' * max_len + ' |')
    
    prior_index = 0
    for i in range(1, trunc + 1):
        if i == trunc:
            print('| ' + string[prior_index:max_len * i] + ' ' * end_spaces + ' |')
        else:
            print('| ' + string[prior_index:max_len * i] + ' |')
        prior_index = max_len * i
    
    print('| ' + ' ' * max_len + ' |')
    print('+-' + '-' * max_len + '-+')

print_box('hello my name is Melvin and I am writing a long message')