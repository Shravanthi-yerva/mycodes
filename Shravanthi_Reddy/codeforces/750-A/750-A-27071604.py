l=list(map(int,input().split(" ")))
n=l[0]
time=l[1]
k=240-time
m=0
total=0
for i in range(1,n+1):
	total=total+5*i
	if(total<=k):
		m=i
	else:
		break
print(m)