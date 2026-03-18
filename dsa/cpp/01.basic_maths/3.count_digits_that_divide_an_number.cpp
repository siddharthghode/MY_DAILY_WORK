/*
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.
*/


#include<bits/stdc++.h>
using namespace std;


int countdigits(int num)
{
int count=0;
int copy=num;
while(num>0)
{
      int digit=num%10;
      num=num/10;
     if(digit !=0 && copy%digit==0)
     {
      count++;
     }
}
return count;
}


int main()
{
    int num=1248;
cout<<countdigits(num);

}
