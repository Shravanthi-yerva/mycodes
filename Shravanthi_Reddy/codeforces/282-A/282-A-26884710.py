i=input()
i=int(i)
x=0
for j in range(0,i):
	s=input()
	if s[1]=='+':
		x=x+1
	else:
		x=x-1

print(x)