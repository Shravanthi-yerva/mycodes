#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,i,j,N,total;
	cin>>n;
	total=0;
	int a[n][n];
	if(n==1)
	{
		cout<<"1"<<endl;
	}
	if(n==2)
	{
		cout<<"2"<<endl;
	}
	if(n==3)
	{
		cout<<"6"<<endl;
	}
    if(n>3)
    {
	for(i=0;i<n;i++)
		{
			a[0][i]=1;
			a[i][0]=1;
		}
	for(i=1;i<n;i++)
	{
		for(j=1;j<n;j++)
		{
			a[i][j]=a[i-1][j]+a[i][j-1];
			if(a[i][j]>total)
			{
				total=a[i][j];
			}
		}
	}
	cout<<total<<endl;
   }
}