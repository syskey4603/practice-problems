def hasDuplicates(nums):
    hashset = set()

    for x in nums:
        if(x in hashset):
            return True
        hashset.add(x)
    return False




nums = [1,2,3,3]
print(hasDuplicates(nums))

