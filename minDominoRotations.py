def minDominoRotations(A, B):   
    # Possible number
    # Most occurning Possible number
    # 6 - most occuring possible number

    maxOccurence = -1
    for i in range(1, 7, 1):
        numOccurence = 0
        for idx, _ in enumerate(A):
            if(A[idx] == i or B[idx] == i):
                numOccurence += 1

        if numOccurence == len(A):

            if(A.count(i) > B.count(i)):
                occurence = A.count(i)
            else:
                occurence = B.count(i)

            if(occurence > maxOccurence):
                maxOccurence = occurence

    if(maxOccurence == -1):
        return -1
    
    minRotations = len(A) - maxOccurence

    return minRotations


# minDominoRotations([2,1,2,4,2,2], 
#                    [5,2,6,2,3,2])

#  

minDominoRotations([3,5,1,2,3],
                   [3,6,3,3,4])

# minDominoRotations([2], [2])