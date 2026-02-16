#include<bits/stdc++.h>
using namespace std;

void star1(int n)
{
  for(int i=0;i<n;i++)
  {
    for(int j=0;j<n-i-1;j++)
    {
      cout<<" ";
    }
    for(int j=0;j<2*i+1;j++)
    {
      cout<<"*";
    }
    for(int j=0;j<n-i-1;j++)
    {
      cout<<" ";
    }
    cout<<endl;
  }
}
void star2(int n)
{
  for(int i=0;i<=n;i++)
  {
    for(int j=0;j<i;j++)
    {
      cout<<" ";
    }
    for(int j=0;j<2*n-(2*i+1);j++)
    {
      cout<<"*";
    }
    for(int j=0;j<i;j++)
    {
      cout<<" ";
    }
    cout<<endl;
  }
  
}
int main()
{
  star1(5);
  star2(5);
  return 0;
}