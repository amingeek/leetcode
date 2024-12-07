nums = [0,0,0,1,2,3,3,3,4,5]
l = len(nums)
if l > 1:
    i = 0
    while(i < l-1):
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
            l -= 1
        else:
            i += 1
print(nums)