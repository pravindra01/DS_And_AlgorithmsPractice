

class soltuion(object):

    # mine naive solution timeout
    def findconsecutiveNumber(self, n):
        while n & 1 == 0:
            print n
            n >>= 1
        print n
        count = 1
        end = (n+1)/2
        for i in range(1, end):
            sum = 0
            for j in range(i, (end+1)):
                sum += j
                if sum > n:
                    break 
                # need to take into consideration that 
                if sum == n:
                    count += 1
                    break 
        return count


    def findconsecutiveNumber2(self,x):
        '''
        Works but not fastest
        '''
        count = 1
        for n in range(2, int((2*x)**0.5)+1):
            if (x-n*(n+1)/2) % n == 0:
                count += 1
        return count

    def consecutiveNumbersSum(self, N ):
        '''
        fastest solution, 
        needed to be math genius to figure this one out
        '''
        while N & 1 == 0: # for numbers like 4,8 it will chnage number to N to 1
            N >>= 1
        ans = 1    
        d = 3  # upto 4 its 1, for 5 condition is covered below, so start while loop with 6
        while d * d <= N:
            e = 0
            while N % d == 0:
                N /= d
                e += 1
            ans *= e + 1
            d += 2

        if N > 1: ans *= 2
        return ans

if __name__ == "__main__":
    test = soltuion()
    for i in range(1,8):
        print("Number: %s, NumConsecutive Ints: %s"%(i,test.findconsecutiveNumber(i)))

