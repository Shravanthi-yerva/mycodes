n=int(input())
a=input()
b=input()
total=0
for i in range(0,n):
	n=int(a[i])
	m=int(b[i])
	if n>m:
		t=n-m
		k=(9-n)+(m+1)
		total=total+min(t,k)
	elif m>n:
		t=m-n
		k=(n-1)+(11-m)
		total=total+min(t,k)
	elif m==n:
		total=total+0
print(total)