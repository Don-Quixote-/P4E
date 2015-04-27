a = 1
b = 2
num = 0
while num <= 4000000: 
	if b % 2 == 0:
		num += b
	elif a % 2 == 0:
		num += a
	a += b
	b += a

print num
