#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        for i in t:
            if i not in s:
                return i
            s.remove(i)
            
        
# @lc code=end

