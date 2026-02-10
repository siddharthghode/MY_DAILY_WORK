#include<bits/stdc++.h>
using namespace std;
int main ()
{   
    cout<<"Give size of 2D array: "<<endl;
    int a,b;
    cin>>a>>b;
    int c[a][b];
    cout<<"Enter elements for 2D array of "<<a<<"X"<<b<<": "<<endl;
    for(int i=0;i<a;i++)
    {
        for(int j=0;j<b;j++)
        {
         cin>>c[i][j];
        }
    }
    cout<<"Entered elements are:"<<endl;
    for(int i=0;i<a;i++)
    {
        for(int j=0;j<b;j++)
        {
         cout<<c[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}