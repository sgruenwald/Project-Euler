from math import log10

def rwh_primes2(n):
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

primes = set(rwh_primes2(1000000))
def check(p):
    for i in xrange(1, int(log10(p)+1)):
        if not (p / 10**i) in primes: return 0
        if not (p % 10**i) in primes: return 0
    return 1

total = 0
for p in primes:
    if p < 10: continue
    if check(p): total += p
print total
