#include<bits/stdc++.h>
using namespace std;

int main()
{
    map<char,int> a;

    string s = "hellowOrld";

    for(int i = 0; i < s.size(); i++)
    {
        a[s[i]]++;
    }

    for(auto it : a)
    {
        cout << it.first
             << " -> "
             << it.second<<endl;
    }
}