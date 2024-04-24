#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = s.split(' ')
        while "" in ls:
                ls.remove("")
        return ' '.join(ls[::-1])
        
# @lc code=end

