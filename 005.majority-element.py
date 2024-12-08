nums = [2,2,1,3,1,1,4,1,1,5,1,1,6]
def majorityElement(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num
        
print(majorityElement(nums))