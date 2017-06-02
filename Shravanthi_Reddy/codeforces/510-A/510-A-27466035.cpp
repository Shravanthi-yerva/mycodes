#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,m,count,total;
	cin>>n>>m;
	count=0;
	total=0;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(i%2==1 && j<=(m-1) && total%2==0)
				{
					if(j==m-1)
					{
						cout<<'#';
					}
					else
					{
					cout<<'.';
					count=count+1;
				    }
				}
		  	if(i%2==1 && j>=0 && j<m && total%2==1 )
				{
					if(j==0)
					{
						cout<<'#';
					}
					else
					{
					cout<<'.';
					count=count+1;
				    }
				}
			if(i%2==0)
			{
				cout<<'#';
				if(count==m-1)
					{
						total=total+1;
						count=0;
					}
			}
			
		}
		cout<<endl;
	}
	
}