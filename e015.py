def score(b) :
	return sum(bb * bb for bb in b)

a = [1]
for i in xrange(20) :
	b = [1] * (len(a)+1)
	for j in xrange(1, len(b)-1) : 
		b[j] = a[j-1] + a[j]
	print b, score(b)
	a = b

"""
#alternatively:
from gmpy import comb

print comb(2 * 20,20)
"""