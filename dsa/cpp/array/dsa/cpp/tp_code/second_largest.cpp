#include <iostream>
using namespace std;
int main()
{
 int a[10]={1,5,3,9,5,2,5,6};
 int big,less_big;
 int length = sizeof(a) / sizeof(a[0]);
 for(int i=0;i<length;i++)
 {
 for(int j=1;j<length;j++)
 {
	 if(a[i]>a[j])
	 {
	 int big = a[i];
     int less_big=a[j];
	 }
	 else if (a[i]<a[j])
	 {
	 int big = a[i];
     int less_big=a[j];
	 }	 
}
}
    cout<<less_big<<endl;
}
