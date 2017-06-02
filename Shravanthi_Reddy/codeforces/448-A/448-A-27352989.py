import math
a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))
cups=sum(a)
medals=sum(b)
k=math.ceil(cups/5)
l=math.ceil(medals/10)
n=int(input())

if k+l>n:
	print("NO")
else:
	print("YES")