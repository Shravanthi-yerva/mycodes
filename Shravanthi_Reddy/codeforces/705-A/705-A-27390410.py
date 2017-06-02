n=int(input())
a="I hate that "
b="I love that "
d="I hate it"
e="I love it"
c=""
if n==1:
	print("I hate it")
else:
	for i in range(1,n):
		if i%2==1:
			c=c+a
		if i%2==0:
			c=c+b
	if n%2==1:
		print(c+d)
	else:
		print(c+e)