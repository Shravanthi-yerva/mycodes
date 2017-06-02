l=list(map(int,input().split(" ")))
n=l[0]
k=l[1]
m=5-k
total=0
a=list(map(int,input().split(" ")))
if m<0:
	print("0")
else:
	for i in a:
		if i<=m:
			total=total+1
print(int(total/3))