#include<bits/stdc++.h>
using namespace std;
int main()
{
    int number= 12345;
    int  get_last_number=number%10;
    cout<<get_last_number<<" now number is:"<<number;
    int remove_last_number=number/10;
    cout<<endl<<remove_last_number;
}