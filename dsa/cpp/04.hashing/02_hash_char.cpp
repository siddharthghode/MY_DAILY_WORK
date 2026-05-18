#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;

    cout << "Enter a string: ";
    cin >> s;

    int hash[256] = {0};

    // Store frequency of characters
    for(char ch : s)
    {
        hash[ch]++;
    }

    int q;

    cout << "How many queries do you want? ";
    cin >> q;

    while(q--)
    {
        char c;

        cout << "Enter character to check frequency: ";
        cin >> c;

        cout << "Frequency of '" << c << "' is: "
             << hash[c] << endl;
    }

    return 0;
}