#!/usr/local/bin/python
# ONly perform + and - 

import math

class Solution(object):

    def calculate(self, expressionStr):
        num = 0
        res = 0
        sign = 1
        stack = []
        i = 0
        for char in expressionStr:
            if char.isdigit():
                # in case is number is more than a signle digit
                num = num * 10 + (ord(char) - ord('0'))
            elif char == '+':
                res += num*sign
                sign = 1
                num = 0
            elif char == '-':
                res += num*sign        
                sign = -1        
                num = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                sign, res = 1,0
                num = 0
            elif char == ')':
                # get sign 
                res += sign*num
                res *= stack.pop()
                res += stack.pop() # add presvios result
                num = 0
        return res + num * sign

if __name__ == "__main__":
    test = Solution()
    print test.calculate("(3 + 2) -1")