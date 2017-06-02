a=input()
total=0
for i in a:
	if i=='h' and total==0:
		total=total+1
	elif i=='e' and total==1:
		total=total+1
	elif i=='l' and total==2:
		total=total+1
	elif i=='l' and total==3:
		total=total+1
	elif i=='o' and total==4:
		total=total+1
if total==5:
	print("YES")
else:
	print("NO")