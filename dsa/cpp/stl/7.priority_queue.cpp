#include<bits/stdc++.h>
using namespace std;
int main()
{  
    //max heap always with greater to smaller
    
    priority_queue<int>pq;
    pq.push(2);
    pq.push(4);
    pq.push(7);
    cout<<pq.top()<<endl;
    pq.pop();
    cout<<pq.top()<<endl;
    pq.pop();
    cout<<pq.top()<<endl;
    pq.pop();
    cout<<pq.top()<<endl;

    //min heap always with smaller to greater 
    priority_queue<int,vector<int>,greater<int>>pq1;
    pq1.push(10);
    pq1.push(2);
    pq1.push(6);
    pq1.push(9);
    pq1.emplace(11);
    while(!pq1.empty())
    {
        cout<<"|"<<pq1.top();
        pq1.pop();
    }
}