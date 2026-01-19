#include<iostream>
#include<string>
using namespace std;
int main()
{
     string a = "madedam";
	int i=0,j=a.length()-1;

	while(i<=j)
	{
      if(a[i]!=a[j]){
		cout<<"Not Pallimdrome"<<endl;
		break;
	}
	else if (a[i]==a[j])
	{
	i++;
	j--;
	if(i==j)
	{
		cout<<"Is Pallimdrome"<<endl;
	}
	}
	
	}
}