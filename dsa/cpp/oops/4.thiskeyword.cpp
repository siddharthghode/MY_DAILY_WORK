#include<bits/stdc++.h>
using namespace std;

class Person{
private:
        int phone_number;
public:
       Person(int phone_number,string name,string lname,int age,int height)
       {
           this->phone_number=phone_number;
           this->name=name;
           this->lname=lname;
           this->age=age;
           this->height=height;
       }
       

       string name;
       string lname;
       int age;
       int height;
       
       void display() {
        cout << "Name: " << name << " " << lname << endl;
        cout << "Age: " << age << endl;
        cout << "Height: " << height << endl;
        cout << "Phone: " << phone_number << endl;
         }

};



int main()
{
    Person p1(1234567890,"abc","xyz",20,5);
    p1.display();

}