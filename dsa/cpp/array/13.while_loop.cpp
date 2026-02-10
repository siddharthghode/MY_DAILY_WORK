#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a;
    getline(cin,a);
    cout<<"String: "<<a;
    cout<<"Third elements: "<<a[2];
    cout<<"All elements: "<<endl;
    int i=0;
    while(i<a.size())
    {
         cout<<i<<":"<<a[i]<<endl; 
         i++;
    }
    return 0;
}