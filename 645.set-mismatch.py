#
# @lc app=leetcode id=645 lang=python
#
# [645] Set Mismatch
#

# @lc code=start
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        duplicate = missing = None

        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        for num in range(1, len(nums) + 1):
            if num not in seen:
                missing = num
                break

        return [duplicate, missing]
        
# @lc code=end

