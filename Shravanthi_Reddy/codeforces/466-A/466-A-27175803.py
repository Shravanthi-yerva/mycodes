l=list(map(int,input().split(" ")))
n_ride=l[0]
sp_ride=l[1]
one_ticket=l[2]
sp_ticket=l[3]
total=0
if(sp_ticket/sp_ride>=one_ticket):
	print(n_ride*one_ticket)
elif sp_ride<=n_ride:
	k=int(n_ride/sp_ride)
	m=n_ride%sp_ride
	total=total+(k*sp_ticket)
	if(sp_ticket>=one_ticket):
		total=total+(m*one_ticket)
		print(total)
	else:
		if m!=0:
			total=total+(sp_ticket)
			print(total)
		if m==0:
			print(total)
elif sp_ride>n_ride:
	if(one_ticket*n_ride>=sp_ticket):
		print(sp_ticket)
	else:
		print(one_ticket*n_ride)