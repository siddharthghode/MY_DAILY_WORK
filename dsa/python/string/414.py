nums=[2,5,7,3,1,3]
first=second=third=0

for i in nums:
    if i>=first:
        third=second
        second=first
        first=i
    elif i>=second and i<first:
        third=second
        second=i
    elif i>third:
        third=i
        
    
if(len(nums)<3):
    print(first)
else:
    print(third)        
