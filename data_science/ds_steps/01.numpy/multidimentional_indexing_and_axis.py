import numpy as np 
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))
print("\n")
print(arr[1:2])
print(arr[0:2,1:3])





arr3d=np.array([[[1,2,3],[4,5,6]],
                [[7,8,9],[10,11,12]]])
print(arr3d.shape)
print(arr3d)
print("\n")
print(arr3d[:,0,:])
print(arr3d[0,1,2])
