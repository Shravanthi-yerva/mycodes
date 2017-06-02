l=list(map(int,input().split(" ")))
s=l[0]
n=l[1]
a=list()
k=0
for i in range(0,n):
	b=list(map(int,input().split(" ")))
	a.append(b)
a.sort(key=lambda x: x[0])
for i in range(0,n):
	if s>a[i][0]:
		s=s+a[i][1]
	else:
		k=1
		print("NO")
		break
if k!=1:
	print("YES")