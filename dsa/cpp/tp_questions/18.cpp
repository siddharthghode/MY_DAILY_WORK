#include<bits/stdc++.h>
using namespace std;
 int main()
 {
    int a,b;
   int  sum=0;
    cout<<"Eneter the numbers that needs to be sum"<<endl;
    cin>>a>>b;
    // while(a<=b)
    // {
    //     sum=sum+a;
    //     a++;
    // }
    while(a<=b)
    {
        sum=sum+(a*a);
        a++;
    }
    cout<<sum;


 }