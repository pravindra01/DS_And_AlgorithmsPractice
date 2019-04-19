

class soltuion(object):

    def findconsecutiveNumber(self, n):
        '''
        finds only signle instance and print it out
        '''
        count = 0
        end = int((n/2) + 1)
        numList = []
        found = False
        #corner case
        if n == 1:
            return 1
        for i in range(1, end):
            sum = 0
            count = 0
            numList = []
            for j in range(i, n):
                sum += j
                if sum > n:
                    break 
                # need to take into consideration that 
                count += 1
                numList.append(j)
                if sum == n:
                    found = True
                    break                                   
            if sum == n:
                break
        if not found:
            numList = []
            count = 0
        print(numList)
        return count

if __name__ == "__main__":
    test = soltuion()
    for i in range(0, 250):
        print("Number: %s, NumConsecutive Ints: %s"%(i,test.findconsecutiveNumber(i)))

