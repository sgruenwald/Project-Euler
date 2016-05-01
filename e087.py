import random

def is_prime3(q,k=50):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    for i in xrange(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

def Euler87():
    below = 50000000
    max = 7072
    numbers = set([])
    prime = [i for i in xrange(1,max) if is_prime3(i)]
    prime2 = [i for i in prime if i ** 3 < below]
    prime3 = [i for i in prime if i ** 4 < below]
    for i in prime3:
        for j in prime2:
            for k in prime:
                S = k ** 2 + j ** 3 + i ** 4
                if S > below: break
                if S not in numbers: numbers.add(S)
    return len(numbers)

def main():
    answer = Euler87()
    print answer
    
if __name__ == "__main__":
    main()