# string to integer
# implement integer parsing function 
# instead of using Library function
import sys
import math

def parseInt(s):
    if s == None or len(s) == 0:
        return 0
    #trim string
    s = s.strip()
    if len(s) == 0:
        return 0
    charIndex = 0
    sign = 1
    if s[charIndex] == '-':
        sign = -1
        charIndex += 1
    elif s[charIndex] == '+':
        sign = 1
        charIndex += 1
    
    result = 0
    while(len(s) > charIndex and s[charIndex] >= '0' and s[charIndex] <= '9'):
        # Multiply by 10 to move to a new decimal place
        result = result * 10 + (ord(s[charIndex]) - ord('0'))
        charIndex += 1
    
    if(sign < 0):
        result = result * sign
    intmax = math.pow(2,31) -1
    if result > intmax:
        return int(intmax)
    
    intmin = -intmax -1
    if result < intmin:
        return int(intmin)

    return int(result)

if __name__ == "__main__":
    print parseInt("   -98765")
    print parseInt("   +567576")
    print parseInt("-99999988999999999999999999999999999")

