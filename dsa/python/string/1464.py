nums=[1,5,4,5]

highest=0
second_highest=0
for i in nums:
    if(i>highest):
        second_highest=highest
        highest=i
    elif(i>second_highest and i<highest):
        second_highest=i
        
print(highest," and ",second_highest)