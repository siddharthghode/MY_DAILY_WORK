#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a;
    getline(cin,a);
    cout<<"String: "<<a;
    cout<<"Third elements: "<<a[2];
    cout<<"All elements: "<<endl;
    for(int i=0;i<a.size();i++)
    {
       cout<<i<<":"<<a[i]<<endl; 
    }
    return 0;
}