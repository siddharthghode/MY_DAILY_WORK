#include<bits/stdc++.h>
using namespace std;

class Teacher{
public:
        
        int salary=30000;
        string name="siddharth";
        string subject="math";

        Teacher()
        {}
        void getinfo()
        {
            cout<<salary<<endl;
            cout<<name<<endl;
            cout<<subject<<endl;
        }
        Teacher(Teacher &cusotm)
        {   
            cout<<"custome constructor called"<<endl;
            salary=cusotm.salary;
            name=cusotm.name;
            subject=cusotm.subject;
        }
        };

int main()
{
   
    Teacher t1;
    //  t1.getinfo();

    Teacher t2(t1);
    t2.getinfo();
    return 0;     
}