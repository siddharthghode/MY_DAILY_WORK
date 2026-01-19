#include<iostream>
using namespace std;
int main()
{
    int a[]={10,15,23,30,42,55,60,75,80,91};
    int count=0;
    for(int i=0;i<20;i++)
    {
        if(a[i]%3==0 && a[i]%5==0)
        {
            count++;
        }
    }
    cout<<"Number of elements divisible by both 3 and 5: "<<count<<endl;
    return 0;
}