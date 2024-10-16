def twosum(nums, target): 
    lowernum = 0
    highernum = len(nums)-1

    nums.sort()
    
    while nums[lowernum] + nums[highernum] != target:
        if(nums[lowernum] + nums[highernum] > target):
            highernum -= 1
        if(nums[lowernum] + nums[highernum] < target):
            lowernum += 1
        if(lowernum >= highernum):
            return -1
        



    return [nums[lowernum], nums[highernum]]





nums = [3,2,3]

target = 6

print(twosum(nums, target))

'''

has to be a sorted list
get a lower and higher pointer 
find the midpoint and if its the target then return
if not then check if the addition is greater or less than the target
if its less then increase the lowerpointer
if its greater reduce the greater pointer
return the lower and higher at the end of the loop

'''