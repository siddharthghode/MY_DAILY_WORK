#include<bits/stdc++.h>
using namespace std;


void printpair()
{
    pair<int,int> p={1,2};
    cout<<p.first<<" "<<p.second<<endl;
    pair<pair<int,int>,int> p1={{2,5},6};
    cout<<p1.first.first<<" "<<p1.first.second<<" "<<p1.second;
}
int main ()
{
    printpair();
    return 0;

}