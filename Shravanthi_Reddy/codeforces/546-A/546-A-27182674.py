l=list(map(int,input().split(" ")))
k=l[0]
n=l[1]
w=l[2]
total=(w*(w+1)*k)/2
if total>n:
	print(int(total-n))
else:
	print("0")