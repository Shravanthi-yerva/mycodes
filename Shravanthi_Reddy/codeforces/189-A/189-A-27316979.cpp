#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n,a,b,c,total;
	cin>>n>>a>>b>>c;
	total=0;
	for(int i=0;i<4001;i=i+a)
	{
		for(int j=0;j<4001;j=j+b)
		{
			if((n-i-j)>=0 and (n-i-j)%c==0)
			{
				total=max(total,(i/a+j/b+(n-i-j)/c));
			}
		}
	}
	cout<<total<<endl;
}