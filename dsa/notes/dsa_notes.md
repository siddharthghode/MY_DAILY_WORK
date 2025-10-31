# The Ultimate DSA Study Guide for Placements

This guide provides a complete roadmap and comprehensive notes for mastering Data Structures and Algorithms (DSA) using C++ for job interviews and competitive programming.

## Table of Contents
1.  [C++ Essentials for DSA](#1-c-essentials-for-dsa)
2.  [C++ Standard Template Library (STL)](#2-c-standard-template-library-stl)
3.  [Time and Space Complexity](#3-time-and-space-complexity)
4.  [Core Data Structures](#4-core-data-structures)
5.  [Essential Algorithms](#5-essential-algorithms)
6.  [Problem-Solving Patterns](#6-problem-solving-patterns)
7.  [50+ Common Interview Questions](#7-50-common-interview-questions)
8.  [Company-Specific Preparation](#8-company-specific-preparation)
9.  [12-Week Structured Study Plan](#9-12-week-structured-study-plan)
10. [Quick Reference Cheat Sheets](#10-quick-reference-cheat-sheets)
11. [Practice Resources & Interview Tips](#11-practice-resources--interview-tips)

---

## 1. C++ Essentials for DSA

Focus only on what's necessary to solve DSA problems efficiently.

* **Basic Syntax**: `main` function, including/using namespaces.
    ```cpp
    #include <iostream>
    int main() {
        std::cout << "Hello, World!" << std::endl;
        return 0;
    }
    ```
* **Data Types**: `int`, `long long`, `char`, `float`, `double`, `bool`. Use `long long` for competitive programming to avoid integer overflow.
* **Control Flow**: `if-else`, `for` loops, `while` loops.
* **Functions**: Pass by value vs. pass by reference (`&`).
    ```cpp
    void modify(int &x) { // Pass by reference
        x = x * 2;
    }
    ```
* **Pointers**: Basic understanding is helpful for Linked Lists and Trees.
* **Arrays & Strings**: Static arrays `int arr[10];` and `std::string`.
* **Structures**: Grouping different data types. Essential for custom types like Tree Nodes.
    ```cpp
    struct Node {
        int data;
        Node* next;
    };
    ```
* **Input/Output**: Use `cin` and `cout`. For faster I/O in competitive programming:
    ```cpp
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    ```

---

## 2. C++ Standard Template Library (STL)

STL is your best friend. Master it.

* **`vector`**: Dynamic array.
    * Syntax: `vector<int> v; v.push_back(10); cout << v[0];`
    * Methods: `push_back()`, `pop_back()`, `size()`, `begin()`, `end()`, `clear()`.
* **`string`**: For string manipulation.
    * Methods: `substr()`, `find()`, `length()`.
* **`stack`**: LIFO (Last-In, First-Out).
    * Syntax: `stack<int> s; s.push(1); s.pop();`
    * Methods: `push()`, `pop()`, `top()`, `empty()`.
* **`queue`**: FIFO (First-In, First-Out).
    * Syntax: `queue<int> q; q.push(1); q.pop();`
    * Methods: `push()`, `pop()`, `front()`, `back()`, `empty()`.
* **`priority_queue`**: A heap-based container. Max-heap by default.
    * Min-heap: `priority_queue<int, vector<int>, greater<int>> pq;`
* **`map` / `unordered_map`**: Key-value pairs.
    * `map`: Sorted keys (Red-Black Tree), $O(\log N)$ operations.
    * `unordered_map`: Unsorted keys (Hash Table), Average $O(1)$ operations.
* **`set` / `unordered_set`**: Stores unique elements.
    * `set`: Sorted, $O(\log N)$ operations.
    * `unordered_set`: Unsorted, Average $O(1)$ operations.
* **`pair`**: Holds two elements.
    * Syntax: `pair<int, string> p = {1, "apple"};`
* **`sort` algorithm**: In `<algorithm>` header. Sorts a container.
    * Syntax: `sort(v.begin(), v.end());`

---

## 3. Time and Space Complexity

The most crucial concept for evaluating solutions.

* **Big O Notation ($O$)**: Describes the **worst-case** scenario.
* **Common Complexities**:
    * $O(1)$: Constant (e.g., accessing an array element)
    * $O(\log N)$: Logarithmic (e.g., binary search)
    * $O(N)$: Linear (e.g., iterating through an array)
    * $O(N \log N)$: Log-linear (e.g., efficient sorting like merge sort)
    * $O(N^2)$: Quadratic (e.g., nested loops, bubble sort)
    * $O(2^N)$: Exponential (e.g., recursive subset generation)
    * $O(N!)$: Factorial (e.g., permutations of a string)

**How to Calculate**: Count the number of operations. A loop from 1 to N is $O(N)$. A nested loop is $O(N^2)$. A recursive call that divides the problem by 2 is $O(\log N)$.

---

## 4. Core Data Structures

| Data Structure | Description | Time Complexity (Avg) | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Array** | Contiguous memory block | Access: $O(1)$ | $O(N)$ |
| **Linked List** | Nodes with data and pointers | Insert/Delete: $O(1)$ (if pointer is known), Search: $O(N)$ | $O(N)$ |
| **Stack** | LIFO data structure | All ops: $O(1)$ | $O(N)$ |
| **Queue** | FIFO data structure | All ops: $O(1)$ | $O(N)$ |
| **Hash Table** | Key-value mapping using a hash function | All ops: $O(1)$ | $O(N)$ |
| **Binary Tree** | Hierarchical structure with nodes having <= 2 children | All ops: $O(N)$ (worst), $O(\log N)$ (balanced) | $O(N)$ |
| **Heap** | A complete binary tree satisfying heap property | Insert/Delete: $O(\log N)$ | $O(N)$ |
| **Graph** | Nodes (vertices) connected by edges | Varies with algorithm (BFS/DFS: $O(V+E)$) | $O(V+E)$ |
| **Trie** | Tree-like structure for efficient string searching | Insert/Search: $O(L)$ where L is key length | $O(N \times L)$ |

### Example: Binary Search Tree (BST) Implementation
```cpp
#include <iostream>
struct Node {
    int data;
    Node *left, *right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

Node* insert(Node* root, int key) {
    if (!root) return new Node(key);
    if (key < root->data) {
        root->left = insert(root->left, key);
    } else {
        root->right = insert(root->right, key);
    }
    return root;
}

void inorder(Node* root) {
    if (!root) return;
    inorder(root->left);
    std::cout << root->data << " ";
    inorder(root->right);
}