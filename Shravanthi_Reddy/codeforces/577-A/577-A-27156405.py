a=list(map(int,input().split(" ")))
n=a[0]
k=a[1]
b=int(k/2)
total=0
for i in range(1,n+1):
	if(k%i==0 and k/i<=n and i<=n):
		total=total+1
print(total)