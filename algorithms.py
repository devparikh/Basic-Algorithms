# Input number n
n=10000000000000

i = 1 
# A loop that runs that says that square of i is smaller than n 
while True:
	square = i**2 
	print(square)
	if n<square:
		break
	i += 1
i -= 1
print(i**2)

