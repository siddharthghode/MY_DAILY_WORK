#include<bits/stdc++.h>
using namespace std;
int main()
{
	list<int> ls;
	ls.push_back(2);
	ls.push_back(4);
	ls.push_back(6);
	ls.push_back(0);
	ls.emplace_back(1);
	cout<<endl<<"print list iteams";
	for(auto it=ls.begin();it!=ls.end();it++)
	{
		cout<<(*it)<<"||";
	}
        cout<<endl<<"sort::";
     ls.sort();
	 for(auto it=ls.begin();it!=ls.end();it++)
	 {
       cout<<(*it)<<"||";
	 }
	 cout<<endl<<"size of list:";
	 cout<<ls.size();
}

