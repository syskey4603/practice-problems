import math
def binarySearch(nums, target):
    lowval = 0
    highval = len(nums)-1
    centerval = math.floor((lowval + highval)/2)
    print(centerval)
    print(nums[centerval])
    while nums[centerval] != target:
        if(nums[centerval] > target):
            highval = centerval
        if(nums[centerval] < target):
            lowval = centerval
        centerval = math.floor((lowval + highval)/2)
        if(lowval + 1 == highval):
            return -1


    return centerval

nums=[-1,0,2,4,6,8]
target=4
print(binarySearch(nums, target))


'''

while the center value is not the target keep going
create low value and high value to find the center
if the nums of centerval == target return centerval 
if numsa of centerval is lower than target make the lowerval = the centerval
if its greater than the target then make the highval the centerval
and find the center again 


'''