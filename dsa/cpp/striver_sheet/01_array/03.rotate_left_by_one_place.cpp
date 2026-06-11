#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> arr={1,2,3,4,5,6,7,8};
    int temp=arr[0];
    for(int i=1;i<=arr.size()-1;i++)
    {
        arr[i-1]=arr[i];
    }
    arr[arr.size ()-1]=temp;
    for(int x=0;x<=arr.size();x++)
    {
        cout<<" "<<arr[x];
    }
}