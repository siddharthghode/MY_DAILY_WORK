nums = [10, 20, 30, 40]
print(nums[0])
print(nums[-4])
nums[1] = 100
nums.append(50)
nums.insert(2, 25)
print(nums)


print("lenght:",len(nums))

#print values 
for num in nums:
    print(num)
    
print("/n")

for i in range(len(nums)):
    print("index:",i,"value:",nums[i])
