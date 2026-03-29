#include <iostream>
#include <vector>
#include <string>

using namespace std;

// 1. Define the structure FIRST
struct Rectangle {
    string name;
    int w; // Width
    int l; // Length
};

int main() {
    // 2. Now the vector knows what a "Rectangle" is
    vector<Rectangle> boxes;

    // Adding data using brace initialization {}
    boxes.push_back({"Shipping Box", 10, 20});
    boxes.push_back({"Gift Box", 5, 5});
    boxes.push_back({"Storage Bin", 40, 60});

    cout << "--- Inventory Dimensions ---" << endl;
    
    // 3. Loop through and display
    for (const auto& box : boxes) {
        cout << "Item: " << box.name << endl;
        cout << "  Width (w):  " << box.w << endl;
        cout << "  Length (l): " << box.l << endl;
        cout << "---------------------------" << endl;
    }

    return 0;
}