#include <iostream>
using namespace std;

int sumOfNumbers(int n) {
    // Base Case: When n reaches 1, we stop and start returning values
    if (n == 1) {
        return 1;
    }
    
    // Recursive Step: n + (sum of all numbers smaller than n)
    return n + sumOfNumbers(n - 1);
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    
    if (n < 1) {
        cout << "Please enter a positive integer.";
    } else {
        cout << "Sum is: " << sumOfNumbers(n);
    }
    
    return 0;
}