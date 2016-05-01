import itertools

n = 5
geom = [[i,n+i,n+(i+1)%n] for i in xrange(n)]
print(max(int(''.join(str(x[i]) for i in sum(geom,[]))) for x in itertools.permutations(xrange(1, 2*n+1)) if x[0] == min(x[:n]) and 10 in x[:n] and len({sum(x[i] for i in g) for g in geom}) == 1))