#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node(int data1, Node *next1)
    {
        data = data1;
        next = next1;
    }
    void print()
    {
        cout << data << endl;
        cout << next;
    }
};
int main()
{
    Node s2(5, nullptr);
    Node s1(6, &s2);
    s2.print();
}