# even numbera at beginning 
# odd at the end
# take time O(n/2)
# O(1) space
# Input : [1,2,3,4,5,6,7,8,9,10]
# Output: [10,2,8,4,6,5,7,3,9,1]


def formatIntArray(arr):
    startIndex = 0
    endIndex = len(arr) -1
    for _ in range(0,len(arr)):
        if startIndex > endIndex:
            break
        print "START: " , arr[startIndex], "Index: ", startIndex
        print "END: " , arr[endIndex], "End Index: ", endIndex
        if (arr[startIndex] % 2) == 0:
            startIndex += 1
        elif (arr[endIndex] % 2) != 0:
            endIndex -=1
        else:
            temp = arr[startIndex]
            arr[startIndex] = arr[endIndex]
            arr[endIndex] = temp
            startIndex +=1
            endIndex -= 1
    return arr

if __name__ == "__main__":
    mynewArr = [1,2,3,4,5,6,7,8,9,10]
    arr = formatIntArrat(mynewArr)
    for item in arr:
        print item