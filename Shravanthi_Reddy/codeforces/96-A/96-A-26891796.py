i=input();
k=len(i);
sum=1;
q=0
for j in range(1,k):
	if i[j]==i[j-1]:
		sum=sum+1
	else:
		sum=1
	if sum>=7:
		q=1
		print("YES")
		break


if q!=1:
	print("NO")