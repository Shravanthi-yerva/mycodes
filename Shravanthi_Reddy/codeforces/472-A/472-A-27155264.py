def is_prime(m):
	if m==2:
		return True
	else:
		k=int(m/2)
		f=0
		for i in range(2,k+1):
			if(m%i==0):
				f=1
				return True
		if(f==0):
			return False
n=int(input())
for j in range(3,n):
	if(is_prime(j) and is_prime(n-j)):
		print(j ,n-j)
		break