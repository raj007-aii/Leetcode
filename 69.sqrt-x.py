#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        guess = x
        while True:
            new_guess = (guess + x // guess) // 2
            if new_guess >= guess:
                return guess
            guess = new_guess
        
# @lc code=end

