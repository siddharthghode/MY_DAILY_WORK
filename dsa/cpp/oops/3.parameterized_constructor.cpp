#include<bits/stdc++.h>
using namespace std;

class Teacher{
private:
        int salary;
        
public:
        Teacher()
        {
            cout<<"Here comes the constructor"<<endl;

        }
        Teacher(int s,string rel)
        {
            salary=s;
            relationship=rel;
        }
        string relationship;
        string name;
        string subject;
        string standard;
        void set_salary(int s)
        {
            salary=s;
        }

        int get_salary()
        {
            return salary;
        }
    };
int main()
{
    Teacher t1(24000,"commited");
    t1.name="siddharth";
    t1.subject="maths"; 
    t1.standard="12th";
    t1.set_salary(25000);
    cout<<t1.get_salary()<<endl;
    cout<<t1.relationship<<endl;


}
