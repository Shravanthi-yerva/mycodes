n=int(input())
total=0
for i in range(0,n):
	l=list(map(int,input().split(" ")))
	p=l[0]
	q=l[1]
	if(p+2<=q):
		total=total+1
print(total)