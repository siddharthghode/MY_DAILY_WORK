#include<bits/stdc++.h>
using namespace std;


 bool comparator(pair<int,int> p,pair<int,int> p1)
   {
      if (p.second<p1.second)return true;
       return false;
   }
int main()
{
   vector<int> v={1,4,5,6,8,2};
   v.push_back(0);
   v.emplace_back(11);
   cout<<v[1]<<endl;

   vector<int>::iterator it;
   for(it=v.begin();it!=v.end();it++)
   {
     cout<<*(it)<<" ";
   }cout<<endl;   

   sort(v.begin(),v.end());
   cout<<"after sorting"<<endl; 
   for(it=v.begin();it!=v.end();it++)
   {
     cout<<*(it)<<" ";
   }
   cout<<endl;
   
   cout<<endl<<"Vectors of pairs"<<endl;
   vector<pair<int,int>> v1={{1,2},{1,1},{1,9},{1,4}};
   cout<<v1[1].second<<endl;
   v1.push_back({1,6});
   v1.push_back({2,1});
   v1.push_back({3,0});
   v1.emplace_back(1,7);
   vector<pair<int,int>>::iterator it1; //print all pairs
   for(it1=v1.begin();it1!=v1.end();it1++)
   {
     cout<<(*it1).first<<" "<<(*it1).second<<"||"; 
   }


   cout<<endl<<"Sorted vector of pairs"<<endl; //print all pairs in sorted order
   sort(v1.begin(),v1.end(),greater<pair<int,int>>());
   for(auto it=v1.begin();it!=v1.end();it++)
   {
      cout<<(*it).first<<" "<<(*it).second<<"||";
   }


   cout<<endl<<"Inverse sorted vector"<<endl; //print all pairs in inverse sorted order
   sort(v1.begin(),v1.end(),greater<pair<int,int >>());
   for(auto it=v1.begin();it!=v1.end();it++)
   {
      cout<<(*it).first<<" "<<(*it).second<<"||";
   }

   cout<<endl<<"Custom sorted vector on the bases of second element"<<endl; //print all pairs in custom sorted order
   sort(v1.begin(),v1.end(),comparator);
   
   for(auto it=v1.begin();it!=v1.end();it++)
   {
      cout<<(*it).first<<" "<<(*it).second<<"||";
   }
   cout<<endl<<"Custom sorted vector on the bases of second element using auto"<<endl; //print all pairs in custom sorted order
     for(auto it:v1)
     {
        cout<<it.first<<" "<<it.second<<"||";
     }
   cout<<endl<<"Size of vector: "<<v1.size()<<endl;
   
}
