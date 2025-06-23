''' Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Questoins I would ask
How big is the array
Can we expect duplicate entries
'''

## Brute Force Solution 1
## I would first pick eat and then sort them - which will give me aet. I will try to loop through next word to check if the sorted of version of it same
## If they are same, i would create a list with aet and store the matching word underneath it
## Time complexity = O(m)*O(logn) = O(mn) and Space Complexity would be O(mn)
from collections import defaultdict
from typing import List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        return list(ans.values())

## Solution 2
## Time complexity = O(m)*O(n) = O(m * log n) and Space Complexity would be O(n)
## Using ASCII code like how we validated Anagram of two string
## What are trying here is to map the ascii for a to z --> 26 character and use index
# For s = "eat"
#                  a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
# count_of_char = {3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}
# letter = Ascii Value = ascii value of char - lowest ascii value(which a=97)
# a = 97 = 97-97 = Index 0
# n = 103 = 103-97 = Index 6
# g = 109 = 109-97 = Index 12
# r = 110 = 110-97 = Index 13
# m = 114 = 114-97 = Index 17
# now each we have list of strings strs = ["eat","tea","tan","ate","nat","bat"]
# what we can do is having hashable list (implemented using dictionary) 
# for each type of sorted words we will have a key value, where key would be count_of_chart() a tuple and values as list of words which maps to the count_of_char
# # ==============================================
# |         Key            |       Value        |
# ==============================================
# | (1,0,0,0,...,0)        | ['eat', 'tea', 'ate']  |
# | (1,0,0,1,0,1,1)        | ['tan', 'nat']         |
# | (1,0,0,0,...)          | ['bat']                |
# ==============================================

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)#creates ans with default one list

        for s in strs: # for each string - create count
            count = [0] * 26
            for char in s: # for each char in string
                count[ord(char) - ord("a")] += 1  # We are storing the count of the char by looping over string s and storing it in the respective tuple index
            ans[tuple(count)].append(s) # Build the ans with word list mapping to the tuple 
        return list(ans.values())




