n=int(input())
d={}
m=list()
l=list(map(int,input().split(" ")))
j=1
for i in l:
	d[i]=j
	j=j+1

for i in range(1,n+1):
	m.append(d[i])

m=map(str,m)
print(' '.join(m))