#Project Euler #2: Even Fibonacci numbers

t=input()
while t>0:
    n=input()
    a=0
    b=1
    c=a+b
    sum=0
    while c<n:
        if c%2==0:
            sum+=c
        a=b
        b=c
        c=a+b
    print sum
    t-=1
