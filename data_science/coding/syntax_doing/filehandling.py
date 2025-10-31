import os 
if os.path.exists('file1.txt'):
    print('file1 exits and available to perform operations')
else:
    print('file1 not fount')
f=open('file1.txt','r')
data=f.read()
print("the data is:")
print(data)
f.close()

a=open('file1.txt','w')
a.write("this is the new data")
a.close()

b=open('file1.txt','r')
data1=b.read()
print("after writting new lines")
print(data1)
b.close()
   

