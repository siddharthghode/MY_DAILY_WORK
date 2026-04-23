#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n=140,c;
    int first=0;
    int second=1;
    cout<<first<<" "<<second<<" ";
    for(int i=2;i<=n;i++)
    {
        c=first+second;
        first=second;
        second=c;
        cout<<c<<" ";
    }
}