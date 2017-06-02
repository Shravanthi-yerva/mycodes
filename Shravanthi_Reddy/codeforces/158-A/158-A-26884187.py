numbers=list(map(int,input().split()));
n=numbers[0];
k=numbers[1];
sum=0;
scores=list(map(int,input().split()));
for i in range(0,n):
	if scores[i]>0:
		if scores[i]>=scores[k-1]:
			sum=sum+1;
			
print(sum);