#include<bits/stdc++.h>
using namespace std;
int main()
{
    int bnum=1011;
    int dnum=0;
    int i=0;
    while(bnum>0)
    {
    int last=bnum%10;
    dnum=dnum+last*pow(2,i);
    bnum=bnum/10;
    i++;
    }
    cout<<"the decimal number is:"<<dnum;
}