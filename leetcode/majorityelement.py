def majorityElement(nums):
    donenums = []
    tempcount = 0
    count = 0
    correctelement = 0
    lenofnums = len(nums)
    for x in range(lenofnums):
        tempcount = 1
        if(nums[x] in  donenums):
            continue
        for y in range(x+1, lenofnums):
            if nums[y] == nums[x]:
                tempcount +=1
        if(tempcount > count):
            count = tempcount
            correctelement = nums[x]
        donenums.append(nums[x])
    return correctelement
        



nums = [1,2,2,3]
print(majorityElement(nums))



'''
check the first element with all other elements if the element is equal to any other number add one to the tempcount
after the element check if tempcount is greater than count if it is then 
replace the tempcount to the count and set temptcount as 0 for the next element and do the same
after checking an element add it to the list and at the start check if any element we are checking is in the list if it is continue if it isnt break 



'''