def isPalin(n):
    return str(n)==str(n)[::-1]

t = input()
palin=[]
for n1 in range(100,1000):
    for n2 in range(100,n1+1):
        m=n1*n2
        if(isPalin(m) and len(str(m))==6):
            palin.append(m)
palin.sort()
                
while t>0:
    t-=1
    n=input()
    i=0
    while i<len(palin):
        if palin[i]>n:
            print palin[i-1]
            break
        i+=1
