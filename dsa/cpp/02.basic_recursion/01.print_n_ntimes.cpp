#include<bits/stdc++.h>
using namespace std;
void recursion_funtion(int i,int n)
{
 
      if(i>n)
      return ;
      cout<<n;
      cout<<endl;
      recursion_funtion(i+1,n);
}

int main()
{
    int n;
    int i=1;
    cout<<"enter the number you want to print n times"<<endl;
    cin>>n;
    recursion_funtion(i,n);
}