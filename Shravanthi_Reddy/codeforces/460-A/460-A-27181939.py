l=list(map(int,input().split(" ")))
n=l[0]
m=l[1]
i=1
socks=n

while(1>0):
	socks=socks-1
	if(i%m==0):
		socks=socks+1
	if(socks==0):
		print(i)
		break
	i=i+1