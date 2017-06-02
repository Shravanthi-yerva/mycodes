l=list(map(int,input().split(" ")))
n=l[0]
m=l[1]
a=list(map(int,input().split(" ")))
total=0
total=total+(a[0]-1)
for i in range(0,m-1):
	if a[i]==a[i+1]:
		total=total
	elif a[i]<a[i+1]:
		total=total+(a[i+1]-a[i])
	else:
		total=(n-a[i])+a[i+1]+total
print(total)