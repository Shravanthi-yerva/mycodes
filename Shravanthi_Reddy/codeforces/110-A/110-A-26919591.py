s=input()
k=len(s)
sum=0
for i in range(0,k):
	if s[i]=='4' or s[i]=='7':
		sum=sum+1
if sum==4 or sum==7:
	print("YES")
else:
	print("NO")