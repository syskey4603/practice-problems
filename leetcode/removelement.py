def removeElement(nums, val):
    for v in range(len(nums)-1, -1, -1):
        if(val == nums[v]):
            nums.pop(v)

    return len(nums)






nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))