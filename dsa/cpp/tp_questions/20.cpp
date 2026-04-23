#include<bits/stdc++.h>
using namespace std;

int main()
{
    int UPPERBOUND,LOWERBOUND;
    int sum=0;

    cin>>UPPERBOUND>>LOWERBOUND;
    for(int i=LOWERBOUND;i<=UPPERBOUND;i++)
    {
       sum=sum+i;

    }
    float average=(double)sum/(UPPERBOUND-LOWERBOUND+1);
    cout<<"THE SUM IS:"<<sum<<endl;
    cout<<"THE AVERAGE IS:"<<average<<endl;



}