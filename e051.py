def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [1] * (n//3)
    sieve[0] = 0
    for i in xrange(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[0]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[0]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n//3-correction) if sieve[i]]

primes = rwh_primes2(230000)

def isprime(num):
    sqrt_n = int(num**.5)
    for p in primes:
        if p > sqrt_n: return 1
        if num % p == 0: return 0
    return 1

def check8(num):
    nstr = str(num)
    slist = list(nstr)
    for old_d in ['0','1','2']:
        if slist.count(old_d) >= 3:
            counter, pnum = 10, [num]
            for new_d in list('0123456789'):
                if new_d != old_d:
                    new_num = int(nstr.replace(old_d, new_d))
                    if new_num < 10000 or not isprime(new_num):
                        counter -= 1
                        if counter<8: break
                    else:
                        pnum.append(new_num)
            if counter >= 8: return pnum
    return 0

def main():
    for p in primes:
        if p < 10000: continue
        result = check8(p)
        if result:
            break
    print result[0]

if __name__ == '__main__':
    main()
