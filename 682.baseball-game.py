#
# @lc app=leetcode id=682 lang=python
#
# [682] Baseball Game
#

# @lc code=start
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores  = []
        idx = 0
        for i in range(len(operations)):
            if operations[i] == '+':
                scores.append(scores[idx-1] + scores[idx-2])
                idx += 1
            elif operations[i] == 'D':
                scores.append(scores[idx-1] * 2)
                idx += 1
            elif operations[i] == 'C':
                scores.pop()
                idx -= 1
            else:
                scores.append(int(operations[i]))
                idx += 1
        return sum(scores)
# @lc code=end

