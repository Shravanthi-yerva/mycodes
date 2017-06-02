n=int(input())
a=list(map(int,input().split(" ")))
a.sort()
a.reverse()
one=0
two=0
three=0
four=0
car=0
for i in a:
	if i==1:
		one=one+1
	if i==2:
		two=two+1
	if i==3:
		three=three+1
	if i==4:
		four=four+1
car=four
four=0
if one>=1 and three>=1:
		if one>three:
			car=car+three
			one=one-three
			three=0
		else:
			car=car+one
			three=three-one
			one=0
car=car+three
three=0
while one>=2 and two>=1:
	car=car+1
	one=one-2
	two=two-1
	

if two>=2:
	k=two/2
	car=car+k
	two=two%2

if one>=4:
	k=one/4
	car=car+k
	one=one%4


while two>=1 and one>=1:
	car=car+1
	one=one-1
	two=two-1
	if one==0 or two==0:
		break

car=car+two
two=0
if one==3:
	car=car+1
	one=0

if one==2:
	car=car+1
	one=0
car=car+one
print(int(car))