def choose(n,k):
	return factorial(n)/factorial(n-k)/factorial(k)
	
def factorial(num):
	return reduce(lambda x,y: x*y,range(1,num+1))
	
A = [1 for i in range(1,101) for j in range(1,i) if choose(i,j)>10**6]

print len(A)