n=int(input())
if n<26:
	a=input()
	print("NO")
else:
	a=input()
	a=a.lower()
	b=[0]*26
	for i in a:
		b[ord('z')-ord(i)]=b[ord('z')-ord(i)]+1
if n>=26:
	k=0
	for i in b:
		if i==0:
			print("NO")
			k=1
			break
	if k!=1:
		print("YES")