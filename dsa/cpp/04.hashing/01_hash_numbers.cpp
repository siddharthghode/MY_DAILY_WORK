#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int arr[n];

    // Input array elements
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    // Hash array for frequency counting
    int hashh[1000000] = {0};

    // Store frequencies
    for(int i = 0; i < n; i++)
    {
        hashh[arr[i]]++;
    }

    int q;
    cin >> q;

    // Answer queries
    while(q--)
    {
        int number;
        cin >> number;

        cout <<"times:"<< hashh[number] << endl;
    }

    return 0;
}