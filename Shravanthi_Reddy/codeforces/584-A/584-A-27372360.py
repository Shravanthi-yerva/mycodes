import math
l=list(map(int,input().split(" ")))
n=l[0]
t=l[1]
a=pow(10,n-1)
b=pow(10,n)
total=0
for i in range(a,b):
	if i%t==0:
		total=1
		print(i)
		break
if total!=1:
	print("-1")