nums = [2,1,5,0]

def canJump(nums):
    n = len(nums)
    max_reach = 0
    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True
    return max_reach >= n - 1

print(canJump(nums))