#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#

# @lc code=start
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s1 = 0
        for i in num1:
            s1 = s1*10 + (ord(i)-48) # 50 - 48 = 2
        s2 = 0
        for j in num2:
            s2 = s2*10 + (ord(j) - 48) # 51 - 48 = 3
        return str(s1*s2)
        
# @lc code=end

