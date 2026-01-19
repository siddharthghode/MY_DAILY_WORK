#include<iostream>
using namespace std;
int main()
{
   int arr[] = {1, 2, 3, 4, 6};
   int odd=0;
   for(int i=0;i<5;i++)
   {
       if(arr[i]%2!=0)
       {
           cout<<"  "<<odd++;
       }
   }
   cout<<odd;
}