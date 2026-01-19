#include <iostream>
using namespace std;

int main() {
    int K;
    int arr[] = {12, 15, 18, 20, 25, 30, 33, 35, 40, 45};
    cout<<"enter the number you want to check and the divisor K: ";
    cin >>K;
    //size of array calculation
    int n = sizeof(arr) / sizeof(arr[0]);

   
    int count = 0;
    for(int i = 0; i < n ;i++) {
        if(arr[i] % K == 0) {
            count++;
        }
    }

    cout << count;
    return 0;
}
