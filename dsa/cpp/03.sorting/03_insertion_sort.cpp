#include<bits/stdc++.h>
using namespace std;

void insertionsort(int arr[],int n)
{
     for(int i=1;i<=n-1;i++)
     {
        int j=i;
        while(j>0 && arr[j]<arr[j-1])
        {
            swap(arr[j],arr[j-1]);    
            j--;      
        }       
        }
     }
int main()
{
    int arr[]={64, 34, 25, 12, 22, 11, 90};
        int n=sizeof(arr)/sizeof(arr[0]);
        insertionsort(arr,n);
        for (int i = 0; i <n; i++)
        {
            cout<<arr[i]<<" ";
        }
}