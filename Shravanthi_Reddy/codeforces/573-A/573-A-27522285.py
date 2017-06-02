a=int(input())
l=list(map(int,input().split(" ")))
k=0
for i in range(0,a):
	while l[i]%2==0:
		l[i]=l[i]/2
	while l[i]%3==0:
		l[i]=l[i]/3
	if i!=0 and k!=1:
		if l[i]!=l[0]:
			print("NO")
			k=1
if k==0:
	print("YES")