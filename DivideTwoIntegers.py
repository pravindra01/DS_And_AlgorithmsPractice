# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# return int max or int min, if result overflows 32 bit integer value


import math

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # check for 0 value
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        #apply sign
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        # check overflow for 32 bit integer
        intmax = math.pow(2,31) -1
        intmin = -intmax -1
        if res > intmax:
            return int(intmax)
        if res < intmin:
            return int(intmin)
        return res

if __name__ == "__main__":
    test = Solution()
    print test.divide(10,3)
    print test.divide(-10,-3)
    print test.divide(10,-3)