# Need to print out a triangle of L and W n
# Need to print out ' ' and then *
# Formula will be one * and the rest ' '
# Then 2 * and the rest ' '
# Or stated differently, n-1 ' ' and 1 *
# Then n-2 ' ' and 2 n etc.

def triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)
    
triangle(5)