#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            return -self.reverse(-x)
        else:
            return int(str(x)[::-1]) if int(str(x)[::-1]) < 2**31 else 0
        
# @lc code=end

