def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in xrange(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n//3-correction) if sieve[i]]

LIMIT = 1000000
primes = rwh_primes2(LIMIT)
primes_set = set(primes)
MAXPRIME = primes[-1]

def isprime(n):
    return n in primes_set

def get_max_consecutive_prime():
    maxlen, maxsum = 21, sum(primes[0: 21])
    while maxsum < MAXPRIME:
        maxlen += 1
        maxsum += primes[maxlen]

    if maxsum == MAXPRIME: return maxsum

    while maxlen:
        maxlen -= 1
        maxsum = sum(primes[0: maxlen])
        if maxsum > MAXPRIME: continue
        if isprime(maxsum): return maxsum
        for start in xrange(1, len(primes) - maxlen):
            maxsum = maxsum - primes[start - 1] + primes[start + maxlen -1]
            if maxsum > MAXPRIME: break
            if isprime(maxsum): return maxsum
    return -1

print(get_max_consecutive_prime())
