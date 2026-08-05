list=[1,1,1,2,2,3] 
k = 2
freq={}

for i in list:
            if(i in freq):
                freq[i]+=1
            else:
                freq[i]=1
        
ans=[]

for i in range(0,k,):
    max_element=None
    max_freq=0
    for i in freq:
     if(freq[i]>=max_freq):
             max_freq=freq[i]
             max_element=i
              
    ans.append(max_element)
    freq.pop(max_element)   


print(ans)