#include<bits/stdc++.h>
using namespace std;
int main()
{
    stack<int> st;
    st.push(1);
    st.push(4);
    st.push(7);
    st.pop();
    stack v=st;
    while(!v.empty())
    {
        cout<<"||"<<v.top();
        v.pop();
    }

}
