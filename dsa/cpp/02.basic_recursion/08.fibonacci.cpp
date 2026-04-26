#include<bits/stdc++.h>
using namespace std;
int fibonacci(int n)
    {
        if(n<=1)
            return n;
        int first=fibonacci(n-1);
        int second=fibonacci(n-2);
        return first+second;
    }
int main()
    {
        cout<<fibonacci(3
);
    }
