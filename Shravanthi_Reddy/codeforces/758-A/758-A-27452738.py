n=int(input())
l=list(map(int,input().split(" ")))
a=max(l)
print((a*n)-sum(l))