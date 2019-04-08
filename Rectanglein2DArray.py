# find rectngle in 2D MAtrix
# Each rectangle is surrounded 1's
# each rectangle comprises of 0's
# [ 1 1 1 1 1 1 1 ]
# [ 1 1 1 1 1 1 1 ]
# [ 1 0 0 0 0 1 1 ]
# [ 1 0 0 0 0 1 1 ]
# [ 1 1 1 1 1 1 1 ]
# return top left and rihgt bottom co-ordinates
#

def findRectangleInMatrix(i, j, matrix, output, index):
    breakFlagRow = False
    breakFlagCol = False
    skipNumber = 2
    for m in range(i, len(matrix)):
        if(matrix[m][j] == 1):
            breakFlagRow = True
            break
        if(matrix[m][j] == skipNumber):
            pass
        for n in range (j, len(matrix[0])):
            if(matrix[m][n] == 1):
                breakFlagCol = True
                break
            else:
                matrix[m][n] = skipNumber
    if breakFlagRow: 
        output[index].append( m-1) 
    else: 
        # when end point touch the boundary 
        output[index].append(m)  
  
    if breakFlagCol: 
        output[index].append(n-1) 
    else: 
        # when end point touch the boundary 
        output[index].append(n)  


def getRectangleCoords(matrix2D):
    sizeOfArray = len(matrix2D)
    matrixCols = len(matrix2D[0])
    output = []
    index = -1
    for i in range(0, sizeOfArray):
        for j in range(0 ,matrixCols):
            if(matrix2D[i][j] == 0):
                output.append([i,j])
                index = index + 1
                findRectangleInMatrix(i, j, matrix2D, output, index)
    print output

if __name__ == "__main__":
    tests = [ 
  
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 0, 0, 0, 1], 
            [1, 0, 1, 0, 0, 0, 1], 
            [1, 0, 1, 1, 1, 1, 1], 
            [1, 0, 1, 0, 0, 0, 0], 
            [1, 1, 1, 0, 0, 0, 1], 
            [1, 1, 1, 1, 1, 1, 1] 
  
        ] 
    getRectangleCoords(tests) 
