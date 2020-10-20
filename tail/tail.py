#
def tail(in_value, n):
    print(in_value)
    print(n)
    if n <= 0:
        return []
    else:      
        if isinstance(in_value, str):
            return ([char for char in in_value])[-n:]
        else:
            return in_value[-n:]


print(tail([1, 2, 3, 4, 5], 3))

print(tail('hello', 2))

print(tail('hello', 0))

print(tail('hello', -2))

#squares = (n**2 for n in range(10))
#print(tail(squares, 3))

print(tail((1, 2, 3), 3), [1, 2, 3])