class Solution:
    
    def mergeSort(self, array):
        if len(array) == 1:
            return array
        
        middleIdx = len(array) // 2
        
        leftSide = array[:middleIdx]
        rightSide = array[middleIdx:]
        
        return self.mergeArrays(self.mergeSort(leftSide), self.mergeSort(rightSide))
    
    def mergeArrays(self, leftSide, rightSide):
        
        leftIdx = 0
        rightIdx = 0
        result = []
        
        while len(leftSide) > leftIdx and len(rightSide) > rightIdx:
            leftDistance = leftSide[leftIdx][0] ** 2 + leftSide[leftIdx][1] ** 2
            rightDistance = rightSide[rightIdx][0] ** 2 + rightSide[rightIdx][1] ** 2
            
            if leftDistance <= rightDistance:
                result.append(leftSide[leftIdx])
                leftIdx += 1
            else:
                result.append(rightSide[rightIdx])
                rightIdx += 1
        
        while len(leftSide) > leftIdx:
            result.append(leftSide[leftIdx])
            leftIdx += 1
        
        while len(rightSide) > rightIdx:
            result.append(rightSide[rightIdx])
            rightIdx += 1
        
        return result
        
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        pointsSortedByDistance = self.mergeSort(points)
        
        return pointsSortedByDistance[:K]