#include<iostream>
using namespace std;

int changevalue(int a)
{
	a=10;
	cout<<"inside fuction a:"<<a<<endl;    
    return a;
}




int main()
{
int a=5;
cout<<"the number before:"<<a<<endl;
changevalue(a);
cout<<"after fuction call:"<<a;
}
	
