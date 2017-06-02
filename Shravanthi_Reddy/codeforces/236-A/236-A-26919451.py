s=input()
s=list(s)
s.sort()
a=''.join(s)
k=len(a)
sum=0
for i in range(0,k-1):
	if a[i]!=a[i+1]:
		sum=sum+1
if sum%2==0:
	print("IGNORE HIM!")
else:
	print("CHAT WITH HER!")