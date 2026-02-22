//leetcode 001th question
/*
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
*/

#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> nums={2,7,11,15};
    int target=17;
     for(int i=0;i<nums.size();i++)
        {
            for(int j=i+1;j<nums.size();j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    cout<<"["<<i<<","<<j<<"]";
                    break;
                }
            }
        }
}

