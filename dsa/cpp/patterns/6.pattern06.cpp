#include<bits/stdc++.h>
using namespace std;

void star()
{
    for(int i=5;i>=1;i--)
    {
        for(int j=1;j<=i;j++)
        {
            cout<<j;
        }
        cout<<endl;
    }
}
int main()
{
    star();
    return 0;
}