def removeDuplicates(nums):
    for x in range(len(nums)-1):
        for y in range(x+1, len(nums)):
            if nums[x] == nums[y]:
                nums.pop(y)
                nums.append('_')
    return nums



nums = [1,1,2]
print(removeDuplicates(nums))



'''

loop through the nums and for each element loop through the rest of the elements
if there is any duplicates replace it with _ and sort it again


'''