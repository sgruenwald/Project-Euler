import numpy as np

def sieve(n):
    sieve = np.ones(n, dtype=bool)
    sieve[::2] = False
    sieve[1] = False
    for i in (i for i in range(3,int(n**0.5)+1,2) if sieve[i]):
        sieve[i*i::2*i] = False
    return np.flatnonzero(sieve)

primes, large_primes = sieve(10**4), set(sieve(10**8))
primes_strings = [str(p) for p in primes]
L = len(primes)

prime_twins = [{j for j in range(1,i) if int(primes_strings[i]+primes_strings[j]) in large_primes and
                                        int(primes_strings[j]+primes_strings[i]) in large_primes}
               for i in range(L)]

def find_family():
    for e in range(5,L):
        for d in prime_twins[e] - {1,3}:
            for c in (prime_twins[d] & prime_twins[e]) - {1}:
                for b in (prime_twins[c] & prime_twins[d] & prime_twins[e]) - {1}:
                    for a in prime_twins[b] & prime_twins[c] & prime_twins[d] & prime_twins[e]:
                        return [primes[x] for x in [a, b, c, d, e]]
prime_list = find_family()
print str(sum(prime_list))
