#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,total,i,j;
	total=0;
	cin>>n;
	int ar[n][2];
	for(i=0;i<n;i++)
	{
		for(j=0;j<2;j++)
		{
			cin>>ar[i][j];
		}
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i==j)
			{
				continue;
			}
			else{
				if(ar[i][0]==ar[j][1])
				{
					total=total+1;
				}
			}
		}
	}
	cout<<total<<endl;
}