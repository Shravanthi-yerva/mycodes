n=list(input())
m=list(input())
k=len(n)
a=list()
for i in range(0,k):
	if n[i]==m[i]:
		a.append('0')
	else:
		a.append('1')
print(''.join(a))