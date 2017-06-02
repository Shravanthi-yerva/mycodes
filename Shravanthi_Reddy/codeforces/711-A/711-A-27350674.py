n=int(input())
total=0
a=list()
k=0
for i in range(0,n):
	l=list(input())
	if (l[0]=='O' and l[1]=='O'):
		l[0]='+'
		l[1]='+'
		total=total+1
		k=1
		a.append(''.join(l))
		break
	elif (l[3]=='O' and l[4]=='O'):
		l[3]='+'
		l[4]='+'
		total=total+1
		k=1
		a.append(''.join(l))
		break
	a.append(''.join(l))
	total=total+1
if total<n:
	for i in range(total,n):
		l=input()
		a.append(l)
if k==1:
	print("YES")
else:
	print("NO")
for i in a:
	if k==1:
		print(''.join(i))