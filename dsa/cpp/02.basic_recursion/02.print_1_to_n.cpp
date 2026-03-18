#include<bits/stdc++.h>
using namespace std;
void print_till_n(int i,int n)
{
    if(i>n)
    return;
    cout<<i<<endl;
    print_till_n(i+1, n);
}
int main()
{
    int i=1,n;
    cout<<"enter the number you want to print from 1 to n:"<<endl;
    cin>>n;
    print_till_n(i,n);
}