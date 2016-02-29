#Project Euler #3: Largest prime factor

import math

#Creating a list of prime factors of the given number
def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num /= i
    if num > 2:
        factors.append(num)

    return factors

t=input()
while t>0:
    t-=1
    n=input()
    factors=prime_factors(n)
    print max(factors)
