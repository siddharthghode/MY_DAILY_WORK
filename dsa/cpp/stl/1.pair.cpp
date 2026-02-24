#include<bits/stdc++.h>
using namespace std;


void printpair()
{
    
    pair<int,int> p={1,2};
    cout<<p.first<<" "<<p.second<<endl;
    pair<pair<int,int>,int> p1={{2,5},6};
    cout<<p1.first.first<<" "<<p1.first.second<<" "<<p1.second<<endl;
    pair<pair<int,int>,pair<int,int>> p3={{1,4},{1,5}};
    cout<<"1st pair 1st element="<<p3.first.first<<" "<<"2nd pair 2nd element="<<p3.second.second<<endl;
    
    pair<int,int> demo={2,5};
    swap(demo,p);
    cout<<p.first<<" "<<p.second<<endl;

    //array of pair
    pair<int,int> arr[]={{1,3},{3,4},{4,5}};
    cout<<arr[1].second<<endl; 

    //bool
    cout<<(p>demo);
}
int main ()
{
    printpair();
    return 0;

}