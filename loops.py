def sum (n):
    s = 0
    for i in range(n):
        s += i + 1
    
    return s

def factorial(n):
    f = 1
    for i in range(n):
        f *= (i + 1)
    
    return f

print(factorial(int(input('Enter a number: '))))
