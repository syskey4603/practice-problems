def singlenumber(nums):
    nums.sort()
    previousequal = False
    for x in range(len(nums)):
        if x == len(nums)-1:
            return nums[x]
        if previousequal == True:
            previousequal = False
            continue
        if nums[x] != nums[x+1]:
            return nums[x]
        else:
            previousequal = True

        


nums = [4,1,2,1,2]
print(singlenumber(nums))

'''
sort it so all doubles are next to each other if x = x + 1 we set previous equal to true 
and go to the next one where we check if previous equal is true if it is set it to false and continue 
if it is the last element we check if previous equal is false 

'''