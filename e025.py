i,t1,t2 = 1,0,1

while len(str(t2))< 1000:
	t1, t2 = t2, t1 + t2
	i += 1

print i