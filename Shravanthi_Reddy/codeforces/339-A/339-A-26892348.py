a=list(input().split("+"))
k=len(a)
b=list(map(int,a))
b.sort()
b=list(map(str,b))
s='+'
c=s.join(b)
print(c)