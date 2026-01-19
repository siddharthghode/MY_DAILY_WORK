#include<iostream>
using namespace std;
int main(){
     int a[]={3,5,7,2,8,6,4,1};
     int max=a[0];
     int min=a[0];
     int n = sizeof(a)/sizeof(a[0]); 
    for(int i = 1; i < n; i++) {
        if(a[i] > max)
            max = a[i];

        if(a[i] < min)
            min = a[i];
    }
cout<<"max"<<max<<endl;
cout<<"min"<<min<<endl;
return 0;           
     
}
