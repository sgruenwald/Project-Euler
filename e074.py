from math import factorial

d = { 169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2 }
def euler74(n) :
	global d
	#print "euler74(%d)" % n
	
	if d.has_key(n) :
		return d[n]
	else :
		new_key = sum(factorial(ord(c) - ord('0')) for c in str(n))
		#print new_key
		d[n] = 0
		result = euler74(new_key) + 1
		d[n] = result
		return result

def testAll ():
	for i in xrange(1, 1000*1000) :
		euler74(i)
	print sum((1 if v == 60 else 0) for v in d.itervalues())

if __name__ == "__main__" :
	testAll()
