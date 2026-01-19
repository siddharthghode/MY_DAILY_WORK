#include<iostream>
using namespace std;
int main()
{
	int arr[5]={10,20,31,40,50};
	int count=0;
	for(int i=0;i<5;i++)
	{
		if(arr[i]%2==0)
		{
		cout<<"Position"<<i<<":"<<arr[i]<<endl;
		count++;
		}
	}
       if(count==0)
       {
	       cout<<"no evne elemnts found";
       }	       

}
