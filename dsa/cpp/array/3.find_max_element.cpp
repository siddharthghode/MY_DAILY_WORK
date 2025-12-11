#include<iostream>
using namespace std;

int main()
{
	int array[] = {10,20,30,40,50,60};
        int max=array[0];
        for(int i=0;i<5;i++)
	{
		if(array[i]>max)
		   max=array[i];
	}
	cout<<"max ="<<max<<endl;
}
