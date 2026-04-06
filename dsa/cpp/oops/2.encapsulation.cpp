#include<bits/stdc++.h>
using namespace std;

class Teacher{
private:
        int salary;
        string relationship;
public:
        Teacher()
        {
            cout<<"Here comes the constructor"<<endl;

        }
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
    Teacher t1;
    t1.name="siddharth";
    t1.subject="maths"; 
    t1.standard="12th";
    t1.set_salary(25000);
    cout<<t1.get_salary()<<endl;


}
