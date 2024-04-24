#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(1, n + 1):
            if p[i - 1] == '*' and dp[0][i - 2]:
                dp[0][i] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
                elif p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]

        
# @lc code=end

