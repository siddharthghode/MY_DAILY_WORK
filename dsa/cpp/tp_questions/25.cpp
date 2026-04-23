#include<bits/stdc++.h>
using namespace std;

int reverse(int arr[],int n)
{
    for(int i=0;i<=n;i++)
    {
        for(int j=n;j>=0;j--)
        {
        swap(arr[i],arr[j]);
        }
        }
    }
int main()
{
    int arr[]={1,2,3,4,5,6};
   int  n=sizeof(arr)/sizeof(arr[0]);

}