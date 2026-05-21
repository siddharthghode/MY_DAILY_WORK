#include<bits/stdc++.h>
using namespace std;

int main()
{
    int arr[] = {1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6};

    int n = sizeof(arr) / sizeof(arr[0]);

    map<int,int> p;

    // Frequency counting
    for(int i = 0; i < n; i++)
    {
        p[arr[i]]++;
    }

    // Printing frequencies
    for(auto it : p)
    {
        cout << it.first
             << " -> "
             << it.second
             << endl;
    }

    int maxFreq = 0;
    int minFreq = n;

    int maxElement;
    int minElement;

    // Finding highest and lowest frequency
    for(auto it : p)
    {
        if(it.second > maxFreq)
        {
            maxFreq = it.second;
            maxElement = it.first;
        }

        if(it.second < minFreq)
        {
            minFreq = it.second;
            minElement = it.first;
        }
    }

    cout << "\nHighest frequency element: "
         << maxElement
         << " Frequency: "
         << maxFreq
         << endl;

    cout << "Lowest frequency element: "
         << minElement
         << " Frequency: "
         << minFreq
         << endl;
}