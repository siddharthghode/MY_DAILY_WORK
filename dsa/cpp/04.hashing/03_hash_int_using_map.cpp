#include<bits/stdc++.h>
using  namespace std;
int main() {
    int arr[] = {1, 2, 2, 1, 9};
    map<int,int> p;
    for(int i=0;i<5;i++){
        p[arr[i]]++;
    }
    for(auto it:p)
    {
        cout<<it.first<<"->"<<it.second<<endl;
    }
    return 0;
}