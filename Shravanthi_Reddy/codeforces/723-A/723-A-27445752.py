l=list(map(int,input().split(" ")))
l.sort()
x1=l[0]
x2=l[1]
x3=l[2]
total=x3
for i in range(x1,x3+1):
	m=abs(i-x1)+abs(i-x2)+abs(i-x3)
	if m<=total:
		total=m
print(total)