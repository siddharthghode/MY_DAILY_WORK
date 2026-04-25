#include<bits/stdc++.h>
using namespace std;

void reverseArray(int arr[],int start,int end)
{
    
    if(start>=end) return;
    swap(arr[start],arr[end]);
    reverseArray(arr,start+1,end-1);
}
int main()
    {
      int arr[]={1,2,3,4,5,6};
      int end=sizeof(arr)/sizeof(arr[0]);
      reverseArray(arr,0,end-1);
      for(int i=0;i<end;i++)
      {
        cout<<arr[i]<<" ";
      }
    }