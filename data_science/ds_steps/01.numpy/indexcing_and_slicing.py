import numpy as np;
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr)
flat=arr.flatten()
new=flat.copy()
print(flat)
print(flat[0])
flat[2]=2222
print(flat)
print(new)
idx=[1,5,3,7]
print(flat[idx])
mask=flat>4
print([mask])
print("------------------------------------------------------------")
print("------------------------------------------------------------")
