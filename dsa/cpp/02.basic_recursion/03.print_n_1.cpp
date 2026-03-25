#include<bits/stdc++.h>
using namespace std;
void print_n_1(int i, int n)
{
    if(i>n)
    return ;
    cout<<n<<endl;
    print_n_1(i, n-1);
    
}
int main()
{
    int i=1,n;
    cout<<"enter the number from which you want to print numbers reverse";
    cin>>n;
    print_n_1(i,n);
}