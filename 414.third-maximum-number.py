#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = second_max = third_max = None
    
        for num in nums:
            if first_max is None or num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num < first_max and (second_max is None or num > second_max):
                third_max = second_max
                second_max = num
            elif second_max is not None and num < second_max and (third_max is None or num > third_max):
                third_max = num
        
        if third_max is None:
            return first_max
        else:
            return third_max
        
# @lc code=end

