#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a[10] = {1,1,2,2,2,3,3,3};

    int i = 0;

    for(int j = 1; j < 8; j++)
    {
        if(a[i] != a[j])
        {
            i++;
            a[i] = a[j];
        }
    }

    for(int k = 0; k <= i; k++)
    {
        cout << a[k] << " ";
    }
}