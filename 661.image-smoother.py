#
# @lc app=leetcode id=661 lang=python
#
# [661] Image Smoother
#

# @lc code=start
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total = count = 0
                for x in range(max(0, i-1), min(m, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        total += img[x][y]
                        count += 1
                result[i][j] = total // count

        return result
                
        
# @lc code=end

