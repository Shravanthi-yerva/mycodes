n=int(input())
a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))
a1=set(a[1:(a[0]+1)])
a2=set(b[1:(b[0]+1)])
a3=a1.union(a2)
s=set()
for i in range(1,n+1):
	s.update([i])
if(s==a3):
	print("I become the guy.")
else:
	print("Oh, my keyboard!")