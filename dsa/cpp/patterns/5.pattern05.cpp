#include<bits/stdc++.h>
using namespace std;

void star()
{
    for(int i=1;i<=5;i++)
    {
        for(int j=5;j>=i;j--)
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