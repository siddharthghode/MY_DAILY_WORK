#include<bits/stdc++.h>
using namespace std;
int partition(vector<int> &arr,int low ,int high)
{
    int pivot=arr[low];
    int i=low;
    int j=high;
    while(i<j)
    {
        while(arr[i]<=pivot && i<=high-1)
        {
            i++;q
        }
        while (arr[j]>pivot && j>=low+1)
        {
            j--;
        }
        if(i<j)
        {
            swap(arr[i],arr[j]);
        }
    }
swap(arr[low],arr[j]);
        return j;
}
void qs(vector<int> &arr,int low,int high)
{
  if(low<high)
  {
    int j=partition(arr,low,high);
    qs(arr,low,j-1);
    qs(arr,j+1,high);
  }
}
int main()
{
    vector<int> arr={34, 7, 23, 32, 5, 62, 78, 1, 55, 19};
    qs(arr,0,arr.size()-1);
    for(auto i:arr)
    {
        cout<<i<<" ";
    }

}
