#include <bits/stdc++.h>
using namespace std;

bool ishappy(int num)
{
    unordered_set<int> seen;   // to detect cycles

    while (true)
    {
        int sum = 0;

        // sum of squares of digits
        while (num > 0)
        {
            int digit = num % 10;
            sum += digit * digit;
            num /= 10;
        }

        // condition 1: if result is 1 → happy
        if (sum == 1)
            return true;

        // condition 2: cycle detected → not happy
        if (seen.count(sum))
            return false;

        // add to set and repeat
        seen.insert(sum);
        num = sum;
    }
}

int main()
{
    cout << ishappy(19);
}