p=2
print(p,'is a prime number')
p+=1

for p in range(3,101,2):

	if p % 3 == 0 and p > 3:
		continue
	if p % 5 == 0 and p > 5:
		continue
	if p % 7 == 0 and p > 7:
		continue
	if p % 9 == 0 and p > 9:
		continue
	print(p,'is a prime number')
