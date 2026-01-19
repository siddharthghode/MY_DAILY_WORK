#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = 5;
    int key = 30;

    int index = -1; 
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            index = i;
            break;
        }
    }

    if (index != -1)
        cout << "Element found at index: " << index;
    else
        cout << "Element not found";

    return 0;
}
