l=[]
for i in range(0,5):
	a=list(map(int,input().split(" ")))
	l.append(a)

mov=0
for i in range(0,5):
	for j in range(0,5):
		if l[i][j]==1:
			row=i
			col=j
			break
k=abs(row-2)+abs(col-2)
print(mov+k)