#include<bits/stdc++.h>
using namespace std;

int main ()
{
    int last_value=500;
     double sumLTR=0.0;
     double sumRTL=0.0;
     double difference;
    for (int i=1; i<=last_value; i++)
    {
        sumLTR +=1.0/i;
    }
    for(int i=last_value;i>=1;i--)
    {
        sumRTL+=1.0/i;
    }
    difference=sumLTR-sumRTL;
    cout<<"the sumLTR is:"<<sumLTR<<" and sumRTL is :"<<sumRTL<<" and the diffrence is:"<<difference;
    return 0;

    }
