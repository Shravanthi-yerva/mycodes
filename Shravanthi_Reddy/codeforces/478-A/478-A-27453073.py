l=list(map(int,input().split(" ")))
k=sum(l)/5
if k==int(k) and k>0:
	print(int(k))
else:
	print("-1")