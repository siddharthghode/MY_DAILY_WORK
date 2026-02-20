#include<bits/stdc++.h>
using namespace std;
int main()
{
    deque<int> dq;
    dq.push_back(3);
    dq.push_front(8);
    dq.emplace_back(1);
    dq.emplace_front(19);
    for(auto it=dq.begin();it!=dq.end();it++)
    {
        cout<<(*it)<<"||";
    }
    cout<<endl;
   sort(dq.begin(),dq.end());
    for(auto it=dq.begin();it!=dq.end();it++)
    {
        cout<<(*it)<<"||";
    }
    cout<<dq.size();
    
}