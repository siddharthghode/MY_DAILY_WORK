class Solution:
    def givesum(self,nums):
      for i in range(1,len(nums)):
        nums[i]=nums[i-1]+nums[i]
        
      return nums



nums=[7, 2, 10, 4, 1, 9, 5, 8, 3, 6]
obj=Solution() 
answer=obj.givesum(nums)
print(answer)

    