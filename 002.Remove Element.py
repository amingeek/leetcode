nums = [0,5,4,8,8,8,7]
val = 8
# return [0,5,4,7,_,_,_]
x = 0
for i in range(0,len(nums)):
    if nums[i] == val:
        x += 1

for i in range(0,x):
    nums.remove(val)
    nums.append("_")
