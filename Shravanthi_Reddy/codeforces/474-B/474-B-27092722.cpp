#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,m,sum,k,f,low,high,i,mid,num;
	cin>>n;
	int l[n];
	int d[n];
	sum=0;
	for(i=0;i<n;i++)
	{
		cin>>l[i];
	}
	for(i=0;i<n;i++)
	{
		sum=sum+l[i];
		d[i]=sum;
	}
	cin>>m;
	for(i=0;i<m;i++)
	{
		cin>>k;
		low=0;
		high=n-1;
		f=0;
		while(low<=high)
		{
			mid=int((high+low)/2);
			if(k>d[mid])
			{
				low=mid+1;
             
            }
            if(k<d[mid])
            {
            	high=mid-1;
            }
            if(low==high && d[low]>=k)
            {
            	f=1;
            	cout<<low+1<<endl;
            	break;
            }
            if(low==high && d[low]<k)
            {
            	f=1;
            	cout<<low+2<<endl;
            	break;
            }
            if(k==d[mid])
            {
            	f=1;
            	cout<<mid+1<<endl;
            	break;
            }
		}
		if (f!=1)
		{
			cout<<low+1<<endl;
		}

	}
	

}