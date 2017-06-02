l=list(map(int,input().split(" ")))
k=l[0]
r=l[1]
for i in range(1,11):
	if ((k*i)%10)==0 or ((k*i)-r)%10==0:
		print(i)
		break