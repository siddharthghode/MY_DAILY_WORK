#include<bits/stdc++.h>
using namespace std;

class Parents{
   public:
          string name;
          int age;

   Parents()
   {
    cout<<"this is parent"<<endl;
   }
   ~Parents()
   {
    cout<<"This is parent dead"<<endl;
   }
};
class Child:public Parents
{
public:
       int rollno;
       Child()
        {
        cout<<"This is child"<<endl;
        }
        ~Child()
        {
            cout<<"This is child dead"<<endl;
        }
};

int main()
{
Child c1;
c1.name="siddharth";
c1.age=23;
c1.rollno=24111042;
cout<<"Name"<<c1.name<<endl;
cout<<"Age"<<c1.age<<endl;
cout<<"Roll no"<<c1.rollno<<endl;
}