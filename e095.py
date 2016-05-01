def create_proper_divisors(limit):
    table = [1] * limit
    for n in xrange(2, limit):
        for m in xrange(n + n, limit, n):
            table[m] += n
    return table

def test() :
	m = 1000 * 1000
	pd = create_proper_divisors(m)
	chains = []
	for i, p in enumerate(pd) :
		#if i % 1000 == 0 :
		#	print ".",
		if p != 1 :
			chain = []
			while True :
				chain.append(i)
				i = pd[i]
				if i > m : break
				elif i in chain :
					j = chain.index(i)
					cc = chain[j : ]
					if len(cc) > 1 :
						chains.append(cc)
						for j in cc :
							pd[j] = 1
					break
	sc = [ (len(chain), min(chain), chain) for chain in chains ]
	print sorted(sc)[-1][1]

if __name__ == "__main__" :
	test()