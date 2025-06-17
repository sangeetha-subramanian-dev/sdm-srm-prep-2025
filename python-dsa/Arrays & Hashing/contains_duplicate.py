## Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
from typing import List
from collections import Counter
class Solution:

## Brute Force Solution
## Time Complexity = O(n^2), Space Complexity = O(n)
    def containsDuplicate1(self, nums: List[int]) -> bool:
        count = 0
        for i in range(0, len(nums)-1): #O(n)
            for j in range(i+1, len(nums)): #O(n)
                if nums[i] == nums[j]:
                    count += 1
                    return True
        return False
    
## Solution 1 using sorting 
## Time complexity: O(nlogn), Space Complexity = O(n)


    def containsDuplicate2(self, nums: List[int]) -> bool:
        count = 0
        nums.sort() # O(nlogn)
        for i in range(0, len(nums)-1): #O(n)
            if nums[i] == nums[i+1]:
                return True
        return False
    
## Solution 2 using sets
## Time complexity: O(n), Space Complexity = O(n)

    def containsDuplicate3(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums: #O(n)
            if num in num_set:
                return True
            num_set.add(num)
        return False


num1 = [1,2,3,1]
num2 = [1,2,3,4]
num3 = [1,1,1,3,3,4,3,2,4,2]
print(Solution.containsDuplicate1(1, num1))
print(Solution.containsDuplicate2(1, num2))
print(Solution.containsDuplicate3(1, num3))