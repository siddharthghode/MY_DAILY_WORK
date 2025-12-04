#include <iostream>
#include <ctime>
using namespace std;

int main() {
    time_t now = time(0);
    cout << "Today: " << ctime(&now);
    return 0;
}

