from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


maximum_number, max_a, max_b = 0, 0, 0
for a in range(-1000, 1000):
    for b in range(0, 1000):
        n = 0
        while is_prime(n ** 2 + (a * n) + b) == True:
            n += 1
        if n > maximum_number:
            maximum_number = n
            max_a, max_b = a, b

print (max_a * max_b)
