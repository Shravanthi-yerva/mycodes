n=int(input())
a=list(map(int,input().split(" ")))
total=0
max=0
for i in range(0,n-1):
	if(a[i+1]>=a[i]):
		total=total+1
	if(total>max):
		max=total
	if(a[i+1]<a[i]):
		total=0
print(max+1)