#include<bits/stdc++.h>
using namespace std;

int pr[1000002]={0};

void seive()
{
	long long int j,m;
	pr[1]=1;
	for(j=2;j<=1000;j++)
	{
		if(pr[j]==0)
		{
		for(m=2*j;m<=1000001;m=m+j)
		{
			pr[m]=1;
		}
	    }
	}
}

int main()
{
	long long int n,i,t,s;
	long long int N;
	seive();
	double k;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>N;
		k=sqrt(N);
		if(k!=ceil(k) or k==1)
		{
			cout<<"NO"<<endl;
		}
        else
        {
            if(pr[(long long)k]==1)
            	cout<<"NO"<<endl;
            if(pr[(long long)k]==0)
            	cout<<"YES"<<endl;

        }


	}

}