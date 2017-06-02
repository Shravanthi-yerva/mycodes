l=list(map(int,input().split(" ")))
n=l[0]
m=l[1]
a=list(map(int,input().split(" ")))
a.sort()
b=max(a)
for i in range(0,(m-n)+1):
	total=a[i+(n-1)]-a[i]
	if total<b:
		b=total

print(b)