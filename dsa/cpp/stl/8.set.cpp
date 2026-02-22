#include<bits/stdc++.h>
using namespace std;
int main()
{
    set<int> s;
    s.insert(1);
    s.insert(4);
    s.insert(6);
    s.insert(1);
    s.insert(10);
    if(s.count(6)){
        cout<<"present"<<endl;
    }
    
}