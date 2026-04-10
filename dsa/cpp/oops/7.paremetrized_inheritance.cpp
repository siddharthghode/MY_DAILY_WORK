#include<bits/stdc++.h>
using namespace std;
   
class teacher{
public:
       string name;
       int age;
    teacher(string name,int age)
    {
      this->name=name;
      this->age=age;
    }
};
class student : public teacher{
public:
       int rollno;
       student(string name, int age,int rollno):teacher(name,age)
       {
           this->rollno=rollno;
       } 
      void getinfo()
       {
            cout<<"Name:"<<name<<endl;
            cout<<"Age:"<<age<<endl;
            cout<<"Rollno"<<rollno<<endl;
       }   
};

int main()
{
student s1("siddharth",23,24111042);
s1.getinfo();

}