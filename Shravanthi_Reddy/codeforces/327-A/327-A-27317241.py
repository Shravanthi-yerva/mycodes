n=int(input())
l=list(map(int,input().split(" ")))
b=list()
count=0
for i in range(0,n):
    if l[i]==1:
        count=count+1
        b.append(-1)
    else:
        b.append(1)
max_ending_here=0
max=0
for i in b:
    max_ending_here=max_ending_here+i
    if max_ending_here<0:
        max_ending_here=0
    if max_ending_here>max:
        max=max_ending_here
while(1>0):
    if n!=1 and count!=n:
        print(max+count)
        break
    if n==1:
        if l[0]==1:
            print("0")
            break
        else:
            print("1")
            break
    if count==n:
        print(n-1)
        break