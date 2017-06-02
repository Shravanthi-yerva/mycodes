n=int(input())
if n==0:
	print("1")
else:
	k=n%4
	if k==1:
		print("8")
	if k==2:
		print("4")
	if k==3:
		print("2")
	if k==0:
		print("6")