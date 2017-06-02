n=int(input())
m=n+1
while 1>0:
	t=list(str(m))
	s=set(str(m))
	if len(s)==len(t):
		print(m)
		break
	else:
		m=m+1