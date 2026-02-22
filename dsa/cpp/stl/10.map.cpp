#include<bits/stdc++.h>
using namespace std;
int main()
{
    map<int,int>mpp;
    mpp.insert({1,4});
    mpp.insert({2,5});
    mpp.insert({3,9});
    mpp.insert({8,10});
    mpp.emplace(1,2);
    // for(auto it:mpp)
    // {
    //     cout<<it.first<<" "<<it.second<<endl;
    // }
    // cout<<endl<<"first key element: "<<mpp[1];
    //  mpp.erase(mpp.begin());
    //   for(auto it:mpp)
    // {
    //     cout<<endl<<it.first<<" "<<it.second<<endl;
    // }
    cout<<mpp[1];
    auto it = mpp.find(2);
    cout<<endl<<(*it).first;
    cout<<endl<<(*it).second;
    auto it1 =mpp.upper_bound(3);
    cout<<endl<<(*it1).first<<" "<<(*it1).second;
}