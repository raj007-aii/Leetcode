#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, curr_subset):
            result.append(curr_subset[:])
            
            for i in range(start, len(nums)):
                curr_subset.append(nums[i])
                backtrack(i + 1, curr_subset)
                curr_subset.pop()

        result = []
        backtrack(0, [])
        return result
        
# @lc code=end

