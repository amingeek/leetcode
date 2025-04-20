nums = [1,2,5,0,1]

def h_index(nums):
    nums = sorted(nums, reverse=True)
    n = 0
    x = 0
    for i in nums:
        n += 1
        if n <= i:
            x += 1
        else:
            return x
    return x

print(h_index(nums))