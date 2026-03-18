#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a=55555;
    int count=0;
    int last_digit=0;
    while(a>0)
    {
         last_digit=a%10;
         count=count+1;
         a=a/10;
    }
    cout<<count;
    cout<<last_digit;
}