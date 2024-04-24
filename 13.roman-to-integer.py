#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate through the string from right to left
        for symbol in reversed(s):
            value = roman_values[symbol]
            # If the current value is smaller than the previous value, subtract it
            if value < prev_value:
                total -= value
            # Otherwise, add it to the total
            else:
                total += value
            prev_value = value

        return total
        
# @lc code=end

