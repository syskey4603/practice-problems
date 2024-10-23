'''
Question:
Given an array nums, move all 0s to the end while maintaining the 
relative order of the non-zero elements.

Test case:
input = [0, 1, 0, 3, 12]
expected_output = [1, 3, 12, 0, 0]

# Test Case 2
input = [0, 0, 0, 0]
expected_output = [0, 0, 0, 0]

# Test Case 3
input = [1, 2, 3, 4]
expected_output = [1, 2, 3, 4]

# Test Case 4
input = [0, 0, 1, 2]
expected_output = [1, 2, 0, 0]

# Test Case 5
input = [1, 2, 3, 0, 0]
expected_output = [1, 2, 3, 0, 0]


Logic: 
use two pointers one to traverse the array and the other to keep the position for the next non zero number
x to traverse y to save the position
if nums[x] != 0 then we do nums[y], nums[x] == nums[x], nums[y] to swap  the position to the unique element
now i add y+=1 and continue

'''


def moveZeroes(nums):
    y = 0
    for x in range(len(nums)):
        if nums[x] != 0:
            nums[y], nums[x] = nums[x], nums[y]
            y+=1
    return nums



input = [0, 1, 0, 3, 12]
print(moveZeroes(input))


