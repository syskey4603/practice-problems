def containsDuplicate(nums):
    nums.sort()
    for x in range(len(nums)):
        if(nums[x]  == nums[x+1]):
            return True
        else:
            continue
    return False




nums = [1,2,3,1]

print(containsDuplicate(nums))