n=int(input())
a=list(map(int,input().split(" ")))
a.sort()
a.reverse()
for i in range(1,n+1):
	if sum(a[0:i])>sum(a[i:n]):
		print(i)
		break