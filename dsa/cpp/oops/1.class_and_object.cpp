#include<bits/stdc++.h>
using namespace std;

class student{
private:
        int age=22;
public:
       string name="siddharth";
       int roll=24111042;
       string lname="ghode";   
       //member function
       int change_roll_number(int newroll)
       {
          roll=newroll;
          return roll;
       }
       string getname()
       {
           return name;
       }
       int getage()
        {
            return age;
        }
       

    };


int main()
{
   student st1;
   st1.change_roll_number(45);
   cout<<st1.roll<<endl;
   cout<<st1.getname()<<endl;
   cout<<st1.getage()<<endl;
   cout<<st1.name<<" "<<st1.lname<<endl;
    return 0;

}