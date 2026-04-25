#include<bits/stdc++.h>
using namespace std;

int main()
{
    int dnum;
    cin>>dnum;
    vector<int> bnum;
    while(dnum>0)
    {
     bnum.emplace_back(dnum%2);
     dnum=dnum/2;
    }
    reverse(bnum.begin(),bnum.end());
    for(auto it:bnum)
    {
        cout<<it;  
    }
}