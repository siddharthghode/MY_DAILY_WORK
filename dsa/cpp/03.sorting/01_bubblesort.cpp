#include<bits/stdc++.h>
using namespace std;


void bubblesort(int arr[],int n)
{
  for(int i=n-1;i>=1;i--)
  {  bool swapped=false;
    for(int j=0;j<i;j++)
    {
        if(arr[j]>arr[j+1])
        {
            swap(arr[j],arr[j+1]);
            swapped=true;
        }
    }
    if(!swapped)
    {
	    break;
    }
  }
}
int main()
{
int arr[]={5,2,9,11,7,0,22};
int n=sizeof(arr)/sizeof(arr[0]);
bubblesort(arr,n);
for(int i=0;i<n;i++)
{
    cout<<" "<<arr[i];
}
}
