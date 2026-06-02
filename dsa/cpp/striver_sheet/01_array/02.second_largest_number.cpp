#include<bits/stdc++.h>
using namespace std;
int main()
{
     int arr[6]={10,3,100,100,2,85};
    int max=arr[0];
    int smax=-1;
    int n=sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<=n-1;i++)
    {
        if(arr[i]>max)
        {
            max=arr[i];
        }
    }
    for(int i=0;i<=n-1;i++)
    {
        if(arr[i]>smax && arr[i]!=max)
        {
            smax=arr[i];
        }
    }
    cout<<"largest element is :"<<max;
    cout<<endl<<"Second largest is"<<smax;
    // cout<<endl<<n;
}