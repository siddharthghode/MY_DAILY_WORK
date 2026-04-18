#include<bits/stdc++.h>
using namespace std;

int main()
{ 
    int num;
    cout<<"Enter the number to get the day"<<endl;
    cin>>num;
    switch(num)
    { case 0:
        cout << "its Monday";
        break;

    case 1:
        cout << "its Tuesday";
        break;

    case 2:
        cout << "its Wednesday";
        break;

    case 3:
        cout << "its Thursday";
        break;

    case 4:
        cout << "its Friday";
        break;

    case 5:
        cout << "its Saturday";
        break;

    case 6:
        cout << "its Sunday";
        break;

    default:
        cout << "Not a valid day";
    }
}