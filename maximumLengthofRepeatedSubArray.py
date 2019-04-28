# Dynamic programming
#

class Solution(object):
    def findLength(self,A,B):
        memo = []
        for _ in range(0, len(A)+1):
            memo.append([0] * (len(B) + 1))
        # now traverese through Lists 
        for i in range(len(A)-1, -1,-1): # max min value 0
            for j in range(len(B)-1,-1,-1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1] +1 # if item already encountered once increment it
        return max(max(row) for row in memo)


if __name__ == "__main__":
    test = Solution()
    A= [1,2,3,2,1]
    B = [3,2,1,1,4,5,6]
    print test.findLength(A,B)