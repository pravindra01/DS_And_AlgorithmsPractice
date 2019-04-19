class Solution(object):

    def getTwoNumSum(self, n, numList):
        _dict = {}
        for i in range(0, len(numList)):
            subnum = n - numList[i]
            try:
                val = _dict.get(subnum, None)
                if val != None and val != i:
                    return (i, val)
            except:
                print "Key not Found ", subnum
            _dict[numList[i]] = i
        raise Exception("wrong Input")


if __name__ == "__main__":
    test = Solution()
    print(test.getTwoNumSum(10 , [2,5,6,7]))