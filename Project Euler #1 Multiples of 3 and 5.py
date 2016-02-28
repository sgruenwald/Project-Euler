def sumn(n, d):    # sum numbers <= n that are divisible by d
    n //= d
    return d*n*(n+1) // 2

t=input()
while t>0:
    t-=1
    L=input()
    a, b =  3, 5

    s = sumn(L-1, a) + sumn(L-1, b) - sumn(L-1, a*b)
    print s
    
            
