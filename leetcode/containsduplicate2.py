'''
without sort
return difference between index of equal elements
shortest distance should be returned between the 2 equal elements.

'''


def containsduplicate2(nums, k):
    shortestdist = 10000000
    if(len(nums) < 2):
        return False
    for x in range(len(nums)-1):
        for y in range(x+1,len(nums)):
            if nums[x]==nums[y] and y-x < shortestdist:
                shortestdist = y-x
    
                
    return shortestdist <= k
       
            




nums = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
k = 1
print(containsduplicate2(nums, k))
'''
first part logic

loop through nums and for each elemnt loop through the rest if an equal element is found return True if not continue
at the end return false

'''