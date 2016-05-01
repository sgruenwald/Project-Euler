from math import sqrt
from fractions import gcd

limit = 1500000

def solve():
    tx = [0] * limit
    for i in xrange(1, int(sqrt(limit)), 2):
	for j in xrange(2, int(sqrt(limit))-i, 2):
	    if gcd(i, j) == 1:
		perimeter = abs(j*j - i*i) + 2*i*j + i*i + j*j
	        for s in xrange(perimeter, limit, perimeter):
		    tx[s] += 1
    return tx.count(1)

if __name__ == '__main__':
    print solve()