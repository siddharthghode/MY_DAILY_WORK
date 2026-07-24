nums = [1,2,3,4,5]

k = 3

window = sum(nums[:k])

for i in range(k, len(nums)):
    window += nums[i]
    window -= nums[i-k]

    print(window)