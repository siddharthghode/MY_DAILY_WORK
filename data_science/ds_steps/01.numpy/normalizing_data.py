import numpy as np

arr = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

mean=arr.mean(axis=0)
std=arr.std(axis=0)
normalised_data=(arr-mean)/std
print(normalised_data)