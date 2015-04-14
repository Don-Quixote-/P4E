nums = list(range(1000))
mtplrs = list()
for x in nums:
	if x % 3 == 0 or x % 5 == 0:
		mtplrs.append(x)
	else:
		mtplrs.append('0')
answer = sum(map(int, mtplrs))
print answer
