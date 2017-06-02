import math
l=list(map(int,input().split(" ")))
n=l[0]
m=l[1]
total=0
for x in range(0,n+1):
	for y in range(0,int(n/2)+1):
		if ((x+y)%m==0 and (x+(2*y)))==n:
			total=1
			print(x+y)
			break
	if total==1:
		break
if total==0:
	print("-1")