d,result={},0

for i in xrange(1,1000):
	d[i**2]=i

for i in xrange(1,1000):
	for j in xrange(1,1000):
		c=i**2 + j**2
		if c in d:
			if i+j+d[c]==1000:
				result=i*j*d[c]
				break

print result