class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if (len(nums) == 0):
            return []
        incrementCounter = nums[0]
        retList = []
        add = True
        lindex = 0
        for i in range(0, len(nums)):
            if incrementCounter == nums[i]:
                if lindex != len(retList) -1:
                    retList.append(str(nums[i]))
                    add = False
                else:
                    add = True
                incrementCounter += 1
            else:
                myVal = retList[lindex]
                if(myVal != str(nums[i-1])): 
                    del retList[lindex]
                    retList.append("%s->%s"%(myVal,nums[i-1]))
                    add = False
                incrementCounter = nums[i] + 1
                lindex += 1
                retList.append(str(nums[i]))
        if add:
            myVal = retList[lindex]
            if(myVal != str(nums[-1])): 
                del retList[lindex]
                retList.append("%s->%s"%(myVal,nums[-1]))
        return retList

if __name__ == "__main__":
    input = [0,2,3,4,6,8,9]
    #Output: ["0->2","4->5","7"]
    test = Solution()
    print test.summaryRanges(input)