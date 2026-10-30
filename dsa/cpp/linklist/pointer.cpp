#include <bits/stdc++.h>
using namespace std;
struct Node
{
    int data;
    Node *next;

    Node(int data1, Node *next1)
    {
        data = data1;
        next = next1;
    }
};

int main()
{
    Node x = Node(1, nullptr);
    Node y = Node(2, &x);
    cout << x.next << endl;
    cout << y.next;
}
