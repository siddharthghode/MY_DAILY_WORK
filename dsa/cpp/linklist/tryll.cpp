#include <bits/stdc++.h>
#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
};

int main()
{
    Node *first = new Node;
    Node *second = new Node;

    first->data = 5;
    second->data = 6;
    first->next = second;
    second->next = nullptr;

    cout << first->data << endl;
    cout << second->data << endl;

    delete first;
    cout << first->data;

    return 0;
}
