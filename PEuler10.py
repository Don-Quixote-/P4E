#This code runs for really really long time.
for p in xrange(2, 2000000):
	for i in xrange(2, p):
		if p % i == 0:
			break	
	else:
		p += p
print p
