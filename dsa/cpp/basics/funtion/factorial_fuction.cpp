#include<iostream>
using namespace std;

int factorial(int n)
{
	int fact=1;
	for(int i=1;i<=n;i++)
	{
		fact=i*fact;
	
	}
	return fact;
}


int main()
{
	int n;
	cout<<"Enter number for factorial"<<endl;
	cin>>n;
	cout<<factorial(n);
}
