#include<bits/stdc++.h>
using namespace std;

void star(int n)
{
   for(int i=0;i<=n;i++)
   {
      //sapces
    //   for(int j=0;j<=i;j++)
    //   {
    //    cout<<" ";
    //   }
      //stars
      for(int k=n;k>=i;k--)
      {
        cout<<"*";
      }
      //spaces
    //   for(int j=0;j<=i;j++)
    //   {
    //    cout<<" ";
    //   }
      cout<<endl;
   }
}
int main()
{
    star(9);
    return 0;
}