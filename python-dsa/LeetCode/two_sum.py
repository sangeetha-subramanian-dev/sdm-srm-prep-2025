'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Questions to ask 

Can i expect only one pair of two sum
Can the array contain duplicate entries?
Do you want the value or the indices itself
Is the order of index important
What is max size of input value
Can i have negative integer
Are we focusin on reducin time complexity here ? if so we should go with hashmap


If the array size is small, brute force is good O(n^2) Time complexity
'''
from typing import List
## Brute Force Solution 1
## Time Complexity = O(n^2), Space Complexity = O(n)
## I would do a for loop and do a inner loop to compare the integer with rest of the integer to see if the target is there
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            target_to_find = target-nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == target_to_find:
                    return [i,j]
## Solution 2
## Time Complexity = O(n), Space Complexity = O(n)
## using Hashmap
class Solution:
    def twoSum_soln2(self, nums: List[int], target: int) -> List[int]:
        index_pair = {}

        for i, num in enumerate(nums): #Iterating through each number in the list nums, i is the index, num is the value at that index, enumerate(nums) is a Pythonic way of getting both the index and value while looping.
            if target - num in index_pair:
                return [i, index_pair[target - num]]
            index_pair[num] = i # If no pair was found, we store the current number and its index so future elements can match against it.


