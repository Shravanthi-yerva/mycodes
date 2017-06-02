n=int(input())
total=1
k=n%4
if k==0:
	total=total+3
else:
	total=total+9
print(total%5)