#Given a compound word and a dictionary  you have to return the words in the dictionary 
# that add up to form the given compound word. 
# e.g. target word = "leetcode" and dict = ["leet", "let", "code", "cod"]

class Solution(object):
    def wordBreak(self, findWord, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        retList = [False] * (len(findWord) + 1)
        i = 0
        retList[0] = True
        for i in range(1,len(findWord)+1):
            for j in range(0,i):
                if retList[j]:
                    if findWord[j:i] in wordDict:
                        retList[i] = True
        return retList[len(findWord)]

if __name__ == "__main__":
    test = Solution()
    print test.wordBreak("leetcode", ["leet","code"])