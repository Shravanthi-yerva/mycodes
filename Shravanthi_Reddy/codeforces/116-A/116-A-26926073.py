n=int(input())
sum=0
total=0
for i in range(0,n):
	a=list(map(int,input().split(" ")))
	k=a[0]
	l=a[1]
	total=total+(l-k)
	if total>sum:
		sum=total
print(sum)