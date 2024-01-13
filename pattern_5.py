n=int(input())
i=1
while i<=n:
	j=1
	while j<=n-i:
		print(" ",end='')
		j=j+1
	a=1
	while a<=i:
		print("*",end='')
		a=a+1
	a=i-1
	while a>=1:
		print("*",end='')
		a=a-1
	print()
	i=i+1
