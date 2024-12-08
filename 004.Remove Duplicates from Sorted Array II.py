nums = [1,1,1,2,2,3]
if len(nums) > 2:
    list1 = []
    for i in range(2,len(nums)):
        if nums[i] == nums[i-2]:
            list1.append(nums[i])
    for i in list1:
        nums.remove(i)
print(list1)