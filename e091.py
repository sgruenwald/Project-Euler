from fractions import gcd

n,t = 50,0
for x in xrange(1, n+1):
    for y in xrange(1, n):
        m = gcd(x,y)
        t += min(x*m/y, m*(n-y)/x)

print t*2 + n*n*3