#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = []
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j]) != 0:
                    if len(strs[j]) >= i+1:
                        if strs[j][i]!= strs[0][i]:
                            return "".join(prefix)
                    else:
                        return "".join(prefix)
                else:
                    return ""
            prefix.append(strs[0][i])
        return "".join(prefix)
        
# @lc code=end

