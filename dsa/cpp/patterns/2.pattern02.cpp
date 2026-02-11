#include<bits/stdc++.h>
using namespace std;

void star()
{
    for(int i=0;i<=5;i++)
    {
        for(int j=0;j<=i;j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
}
int main()
{
    star();
    return 0;
}