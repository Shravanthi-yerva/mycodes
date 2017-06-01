n=int(input())
a=list(map(int,input().split(" ")))
d={}
z=0
for i in a:
	if i>z:
		z=i
	d[i]=d.get(i,0)+1
f0=0
f1=d.get(1,0)
print(d)