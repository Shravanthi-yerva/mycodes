li=list(map(int,input().split(" ")))
n=li[0]
l=li[1]
b=list()
maximum=0
f=0
g=0
f1=0
g1=0
a=list(map(int,input().split(" ")))
a.sort()
for i in range(0,n):
	if i!=n-1:
		dist=a[i+1]-a[i]
		if dist>maximum:
			maximum=dist
	if a[i]==0:
		f=1
	if a[i]==l:
		g=1
if f==0:
	f1=a[0]
if g==0:
	g1=l-a[n-1]
print(max(maximum/2,f1,g1))