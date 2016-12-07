#include <stdio.h>
#include <string.h>
int main()
{

     int a,b,c,d,e,total,sum,no,max,i,j,k;
     total=0;
     no=0;
     max=0;
     scanf("%d",&a);
     scanf("%d",&b);
     char main[a][b+1];
     
     
     	for(i=0;i<a;i++)
     	{
     		for(j=0;j<b;j++)
     		{
     			scanf("%c",&main[i][j]);
     		}
     	}
     	printf("I am printing\n");
     printf("%c\n",main[1][2]);
     printf("%c\n",main[2][3]);

     for(i=0;i<(a-1);i++)
     {
     	
        

        for(k=i+1;k<a;k++)
       { 	
     	    for(j=0;j<b;j++)
     	           {
     		             sum=main[i][j]+main[k][j];
     		             if(sum==1 || sum==2 )
     		             {
     		                     total=total+1;
     		             }
                  }
              if(total>max)
                {
       	           max=total;
       	           no=no + 1;
                }
                total=0;
       
       }
      
           

     }

   printf("%d\n",no);
}