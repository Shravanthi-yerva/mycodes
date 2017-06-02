n=int(input())
l=list(map(int,input().split(" ")))
if(sum(l)<n):
	print("-1")
else:
	l.sort()
	l.reverse()
	for i in range(0,13):
		if sum(l[0:i])>=n:
			print(i)
			break