class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        squaredA = []
        for num in A:
            squaredA.append(num ** 2)
        

        return sorted(squaredA)

            
        