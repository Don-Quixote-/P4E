m = 600851475143
n = 2
while n <= m:
	if m % n == 0:
		m = m / n
	n += 1
print n - 1  # the n for now is the n+1 where we stop, so the real n we want supposed to be (n+1)-1 which is n-1. 
