#include<bits/stdc++.h>
using namespace std;

void star()
{
   for(int i=1;i<=5;i++)
   {
      //spaces  
    for(int j=5;j>=i;j--)
      {
        cout<<" ";
      }
      //stars
    for(int j=1;j<=2*i-1;j++)
    {
        cout<<"*";
    }
      //spaces
    for(int j=5;j>=i;j--)
      {
        cout<<" ";
      }
      cout<<endl;
   }
}
int main()
{
    star();
    return 0;
}