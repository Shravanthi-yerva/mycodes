a=list(map(int,input().split(" ")))
n=a[0]
m=a[1]
total=0
while(n>0 and m>0 and n+m>=3):
	if n>=m and n>=2:
		n=n-2
		m=m-1
		total=total+1
	if m>n and m>=2:
		m=m-2
		n=n-1
		total=total+1
print(total)