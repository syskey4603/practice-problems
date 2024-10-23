def twosum(nums, target): 
    lenofnum = len(nums)
    for x in range(0, lenofnum-1):
        for y in range(x+1, lenofnum):
            temptarget = nums[x] + nums[y]
            if(temptarget == target):
                return x, y



nums = [3,2,3]

target = 6

print(twosum(nums, target))
'''
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''

