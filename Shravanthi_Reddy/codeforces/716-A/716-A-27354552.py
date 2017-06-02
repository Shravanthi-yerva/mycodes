l=list(map(int,input().split(" ")))
n=l[0]
c=l[1]
a=list(map(int,input().split(" ")))
k=0
for i in range(1,n):
	if a[i]-a[i-1]>c:
		k=i
print(n-k)