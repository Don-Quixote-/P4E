num1 = 1
num2 = 2
num = list()
while num1 <= 4000000:
	num.append(num1)
	num.append(num2)
	num1 += num2
	num2 += num1

answer = 0
for i in num:
	if i % 2 == 0:
		answer += i
print answer
