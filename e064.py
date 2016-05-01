from __future__ import division
from math import ceil,floor,sqrt

limit = 10000

def solve():
    count = 0
    for S in range(2,limit+1):
        a0 = floor(sqrt(S))
        # perfect squares aren't irrational
        if a0*a0 != S: 
            length = 0
            m = 0
            d = 1
            a = a0
            # new termination conditiona quits one iteration early
            while a != 2*a0: 
                length += 1
                m = d * a - m
                d = (S - m*m) / d
                a = floor((a0 + m)/d)
            # because of termination condition, length is accurate
        if length & 1:
            count += 1
    return count

if __name__ == '__main__':
    print solve()