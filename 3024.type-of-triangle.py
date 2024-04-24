#
# @lc app=leetcode id=3024 lang=python
#
# [3024] Type of Triangle
#

# @lc code=start
class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) < 3:
            return "Not a triangle"
        if nums[0] + nums[1] > nums[2]:
            return "Not a triangle"
        if nums[0] + nums[2] > nums[1]:
            return "Not a triangle"
        if nums[1] + nums[2] > nums[0]:
            return "Not a triangle"
        if nums[0] == nums[1] == nums[2]:
            return "Equilateral"
        if nums[0] == nums[1]:
            return "Isosceles"
        if nums[0] == nums[2]:
            return "Isosceles"
        if nums[1] == nums[2]:
            return "Isosceles"
        
# @lc code=end

