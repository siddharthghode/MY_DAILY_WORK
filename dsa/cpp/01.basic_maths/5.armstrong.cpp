//myyy easiest way
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n=153;
    int copy_n=n;
    int count=0;
    int digit=0;
    int sum=0;
    while(n>0)
    {   
        count=count+1;
        n=n/10;
        
    }
    int n1=copy_n;
    while(n1>0)
    {
       digit=n1%10;
       sum+=pow(digit,count);
       n1=n1/10;
    }
    if(sum==copy_n)
    {
        cout<<"yes it is armstrong";
    }
    else cout<<"it is not armstrong";
    // cout<<count<<endl;
    cout<<n;
}

/*
easy way to count digits
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n = 153;
    int copy = n;
    int sum = 0;

    int digits = log10(n) + 1;

    while(n > 0)
    {
        int digit = n % 10;
        sum += pow(digit, digits);
        n /= 10;
    }

    if(sum == copy)
        cout << "Yes it is Armstrong";
    else
        cout << "Not Armstrong";
}
*/
/*
more easy way and compitative 
#include<bits/stdc++.h>
using namespace std;

int main() {
    int n = 153, copy = n, sum = 0, digits = log10(n) + 1;

    while(n){
        sum += pow(n%10, digits);
        n /= 10;
    }

    cout << (sum == copy ? "yes it is armstrong" : "it is not armstrong");
}
*/