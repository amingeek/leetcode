nums = [2,3,1,1,4]
# nums = [2,0]

def jump(nums):
    n = len(nums)
    location = 0
    if len(nums) == 1:
        return True
    
    elif n >= 2:
        while True:
            try:
                if location == n - 1:
                    return True
                if nums[location] == 0 and location != n - 1:
                    return False
                
                location += nums[location]
            except:
                return False
            

print(jump(nums))