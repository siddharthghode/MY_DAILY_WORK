#include<bits/stdc++.h>
using namespace std;
int main()
{   
    int temp=0;
    vector<int> a={0,1};
    for(int i=0;i<a.size()-1;i++)
    {
        if(a[i]==a[i+1])
        {
            a[i]=a[i]*2;
            a[i+1]=0;
        }
    }
   int n = a.size();

    vector<int> ans(n, 0);   // all zeros
    int idx = 0;             // place non-zero here

    for (int i = 0; i < n; i++) {
        if (a[i] != 0) {
            ans[idx] = a[i];
            idx++;
        }
    }

    for (int x : ans) cout << x << " ";
   
    // for (int x : a)
    // cout << x << " ";
   
}