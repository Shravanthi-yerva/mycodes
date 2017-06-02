n=int(input())
police=0
untreat=0
l=list(map(int,input().split(" ")))
for i in l:
	if i>=0:
		police=police+i
	elif i==-1 and police>0:
		police=police-1
	elif i==-1 and police<=0:
		untreat=untreat+1
print(untreat)