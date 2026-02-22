#include<bits/stdc++.h>
using namespace std;
int main()
{
  multiset<int> mset;
  mset.insert(4);
  mset.insert(4);
  mset.insert(5);
  for(int x:mset)
  {
    cout<<x<<" ";
  }
}