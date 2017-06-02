l=list(map(int,input().split(" ")))
n=l[0]
d=l[1]
a=list(map(int,input().split(" ")))
if sum(a)+(10*(n-1))>d:
	print("-1")
else:
	k=sum(a)+(10*(n-1))
	l=d-k
	print((n-1)*2+int(l/5))