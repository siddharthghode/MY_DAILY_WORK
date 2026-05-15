import time

def bubblesort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [5, 2, 9, 11, 7, 0, 22]

# ⏱ Start time
start = time.time()

bubblesort(arr)

# ⏱ End time
end = time.time()

print("Sorted array:", arr)
print("Time taken:", (end - start), "seconds")