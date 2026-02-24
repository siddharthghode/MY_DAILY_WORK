#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> a={9,36,0,28,47,33,21,3,23,49};
    int count_even=0;
    int count_odd=0;
    for(int i=0;i<a.size();i++)
    {
        if(a[i]%2==0)
        {
           count_even=count_even+1;
          
        }
       else
       count_odd=count_odd+1;
    }
    cout<<count_even;
    cout<<endl<<count_odd;
}