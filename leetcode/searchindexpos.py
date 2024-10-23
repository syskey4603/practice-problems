def searchInsert(nums,target):
    for x in range(len(nums)):
        if nums[x] == target:
            return x
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)



nums = [1,3,6]
target = 5

print(searchInsert(nums, target))


'''
loop through the list find if nums[x] = target return x if not add x to the list and sort it


'''