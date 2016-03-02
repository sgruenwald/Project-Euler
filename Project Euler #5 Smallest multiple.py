def GCD(M, N):
    while (N != 0):
        M, N = N, M % N
    return M
 

t=input()
while t>0:
    t-=1
    n=input()
    

    LCM = 1
    for X in xrange(1, n+1):
        LCM = (X * LCM)/GCD(X, LCM)
    print LCM
    
