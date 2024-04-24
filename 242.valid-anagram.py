#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(map(lambda i:i, s))
        t = list(map(lambda i:i, t))
        return sorted(s) == sorted(t)
        
# @lc code=end

