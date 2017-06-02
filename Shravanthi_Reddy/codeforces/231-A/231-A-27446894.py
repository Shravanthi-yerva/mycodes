n=int(input())
total=0
for i in range(0,n):
	a=list(map(int,input().split(" ")))
	k=sum(a)
	if k>=2:
		total=total+1

print(total)