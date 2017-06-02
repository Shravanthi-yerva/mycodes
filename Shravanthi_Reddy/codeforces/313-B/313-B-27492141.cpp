#include<bits/stdc++.h>
using namespace std;
int main()
{
	string a;
	int n,i,j,total,m,t,s;
	cin>>a;
	n=a.length();
	int l[n];
	total=0;
	l[0]=0;
	j=1;
	for(i=0;i<n-1;i++)
	{
		if(a[i]==a[i+1])
		{
			total=total+1;
		}
		l[j]=total;
		j=j+1;
	}
	cin>>m;
	for(i=0;i<m;i++)
	{
		cin>>t;
		cin>>s;
		cout<<l[s-1]-l[t-1]<<endl;
	}




}