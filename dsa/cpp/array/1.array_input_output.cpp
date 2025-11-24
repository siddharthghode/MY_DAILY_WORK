#include<iostream>
using namespace std;
int main(){
    int n;
    int a[n];
    cout <<"enter thr number of aaray  you want to create "<<endl;
    cin>>n;
    //enter elements in array
    cout<<"enter"<<n<<"elements \n"<<endl;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    //print elements of aaray
    cout<<"the elements in aaray are: \n"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
}