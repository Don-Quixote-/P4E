# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

li = []
mli = []

for x in range(900, 1000):
	for y in range(900, 1000):
		p = x * y
		if str(p)[0] == str(p)[-1] and str(p)[1] == str(p)[-2]:
			li.append(p)

for m in li:
	if str(m)[2] == str(m)[-3]:
		mli.append(m)
print(mli)
