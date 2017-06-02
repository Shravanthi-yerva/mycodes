n=int(input())
l=list(map(int,input().split(" ")))
even=0
odd=0
okey=0
ekey=0
for i in range(0,n):
	if(l[i]%2==0):
		ekey=i
		even=even+1
	else:
		okey=i
		odd=odd+1
	if even>1 and odd>0:
		print(okey+1)
		break
	if odd>1 and even>0:
		print(ekey+1)
		break