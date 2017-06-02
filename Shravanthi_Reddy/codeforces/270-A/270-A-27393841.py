n=int(input())
for i in range(0,n):
	N=int(input())
	t=360/(180-N)
	if t>=1 and int(t)==t:
		print("YES")
	else:
		print("NO")