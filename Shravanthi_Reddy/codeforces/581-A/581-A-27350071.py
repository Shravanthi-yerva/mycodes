l=list(map(int,input().split(" ")))
a=l[0]
b=l[1]
if a>=b:
	diff=b
	b=0
	a=a-diff
	same=int(a/2)
else:
	diff=a
	a=0
	b=b-diff
	same=int(b/2)
print(diff, same)