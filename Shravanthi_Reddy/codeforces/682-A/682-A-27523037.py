l=list(map(int,input().split(" ")))
n=l[0]
m=l[1]
a=list()
b=list()
total=0
if m>=n:
	for i in range(1,n+1):
		a.append(i%5)
		b.append(i%5)
	for i in range(n+1,m+1):
		b.append(i%5)
else:
	for i in range(1,m+1):
		a.append(i%5)
		b.append(i%5)
	for i in range(m+1,n+1):
		a.append(i%5)
if a.count(0)>0 and b.count(0)>0:
	total=total+a.count(0)*b.count(0)
if a.count(1)>0 and b.count(4)>0:
	total=total+a.count(1)*b.count(4)
if a.count(2)>0 and b.count(3)>0:
	total=total+a.count(2)*b.count(3)
if a.count(3)>0 and b.count(2)>0:
	total=total+a.count(3)*b.count(2)
if a.count(4)>0 and b.count(1)>0:
	total=total+a.count(4)*b.count(1)
print(total)