'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: 
What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?'''



from collections import Counter
class Solution:

## Solution 1 - Collection Counter
## Time Complexity = O(n), Space Complexity = O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
## Solution 2 - Using Hash
## Time Complexity = O(n^2), Space Complexity = O(n) O(26)
## We are going tp use dictionary/Hashmap because we can compare number of times the character has appeared easily with key character
## In case of s = "anagram"
## counter = {"a": 3, "g": 1, "m": 1, "n": 1, "r": 1}

    def isAnagram_soln2(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter = {}
        for char in s:  #O(n)
            counter[char] = counter.get(char, 0) + 1
        for char in t:  #O(n)
            if char not in counter or counter[char]==0:
                return False
            else:
                counter[char]-=1
        return True
    
## Solution 3 - Using Ascii Values
## Time Complexity = O(n), Space Complexity = O(n)
## What are trying here is to map the ascii for a to z --> 26 character and use index
# For s = "anagram"
#                  a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
# count_of_char = {3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}
# letter = Ascii Value = ascii value of char - lowest ascii value(which a=97)
# a = 97 = 97-97 = Index 0
# n = 103 = 103-97 = Index 6
# g = 109 = 109-97 = Index 12
# r = 110 = 110-97 = Index 13
# m = 114 = 114-97 = Index 17
    def isAnagram_sol3(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            count = [0] * 26 # for storing the char count based on index as ascii value of it
            for char in s:
                count[ord(char)-ord('a')]+=1 # We are storing the count of the char by looping over string s and storing it in the respective index
            for char in t:
                if count[ord(char)-ord('a')]==0:
                    return False
                else:
                    count[ord(char)-ord('a')]-=1
            return True
