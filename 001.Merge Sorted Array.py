def array_merge(a1, a2):
    array = []
    for i in a1:
        if i != 0:
            array.append(i)
    for i in a2:
        if i != 0:
            array.append(i)
    return array
def sorting(array):
    if len(array) > 1:  
        for i in range(0,len(array)-1):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
    return array
nums1 = [0]
nums2 = [1]

array = array_merge(nums1,nums2)
print(sorting(array))