from math import sqrt

def isPrime (n):
    if n == 1: return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

x = int(input('Get Primes until: '))

print(2, end=' ') if x >= 2 else None

for i in range(3, x + 1, 2):
    if isPrime(i):
        print(i, end=' ')