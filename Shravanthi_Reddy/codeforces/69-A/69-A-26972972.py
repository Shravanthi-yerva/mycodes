n=int(input())
l=[]
for i in range(0,n):
	a=list(map(int,input().split(" ")))
	l.append(a)
x=[]
total=0
for j in range(0,3):
	for i in range(0,n):
		total=total+l[i][j]
	x.append(total)
	total=0
if x[0]==0 and x[1]==0 and x[2]==0:
	print("YES")
else:
	print("NO")