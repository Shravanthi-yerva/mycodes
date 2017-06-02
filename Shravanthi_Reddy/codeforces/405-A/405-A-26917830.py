n=int(input())
a=list(map(int,input().split(" ")))
a.sort()
a=list(map(str,a))
k=' '
print(k.join(a))