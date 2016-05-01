from itertools import *

def get_digits(n):
    return [int(digit) for digit in str(n)]

def main():
    largest = 0
    for a, b in product(range(1, 100), range(1, 100)):
        s = sum(get_digits(a ** b))
        if s > largest:
            largest = s
    print largest

if __name__ == "__main__":
    main()