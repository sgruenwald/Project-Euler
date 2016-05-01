s,mod = 0,10**10

for x in xrange(1, 1001):
    s += pow(x, x, mod)

print s%mod