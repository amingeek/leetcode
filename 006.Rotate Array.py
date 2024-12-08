nums = [1,2]
k = 3

def rotate(nums, k):
    n = len(nums)
    if n <= 1: 
        return nums
    k %= n  
    for _ in range(k):
        nums.insert(0, nums.pop())
    
    return nums

print(rotate(nums, k))