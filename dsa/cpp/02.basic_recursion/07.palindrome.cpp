#include<bits/stdc++.h>
using namespace std;

bool check_palindrome(string word, int i, int end)
{
    if(i >= end) return true;

    if(word[i] != word[end]) return false;

    return check_palindrome(word, i + 1, end - 1);
}

int main()
{
    string word = "madam";
    int end = word.size();

    if(check_palindrome(word, 0, end - 1))
        cout << "Palindrome\n";
    else
        cout << "Not Palindrome\n";
}