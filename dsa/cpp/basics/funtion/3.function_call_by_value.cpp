#include<bits/stdc++.h>
using namespace std;
int changenumber(int a)
{
    a = 100;
    return a;
}
int main()
{
    int a = 10;
    cout<<"Before changing the number: "<<a<<endl;
    int newnumber = changenumber(a);
    cout<<"After changing the number: "<<a<<endl;
    cout<<"The new number is: "<<newnumber;
    return 0;
}