#Two Number Sum
#Problem Statement
#Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order. 
# If no two numbers sum up to the target sum, the function should return an empty array. 
# Assume that there will be at most one pair of numbers summing up to the target sum.

#Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 Sample output: [-1, 11]

# Method 1 - for loops 

def two_num_sum(array,targetSum):
    for i in range (len(array)-1):
        firstNum = array[i]
        for j in range (i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]

# Time Complexity = O(n^2)  Space Complexity = O(1)


# Method 2 - Hash Table 

def two_num_sum(array, targetSum):
    nums ={}
    for num in array:
        num2 = targetSum - num
         if num2 in nums:
             return [num, num2]
        else:
            nums[num] = True
    return []

# Time Complexity = O(n)    Space Complexity = O(n)

# Method 3 - With Sorting 

def two_num_sum(array, two_num_sum):
    array.sort()
    left = 0
    right = len(array)
    while left<right:
        if targetSum == array[left] + array[right]:
            return [array[left], array[right]]
        elif targetSum > array[left] + array[right]:
            left += 1
        elif targetSum < array[left] + array[righ]:
            right -= 1
    return[]

# Time Compleity =  O(nlog(n))  Space Complexity = O(1)

