class Solution(object):
    def sortedSquares(self, A):
        
        N = len(A)
        j = 0

        
        arr = []


        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        while i >= 0 and j < N:
            if A[i] ** 2 < A[j] ** 2:
                arr.append(A[i] ** 2)
                i -= 1
            else:
                arr.append(A[j] ** 2)
                j += 1
        
        while i >= 0:
            arr.append(A[i] ** 2)
            i -= 1

        while j < N:
            arr.append(A[j] ** 2)
            j += 1
        
        return arr
                


solution = Solution().sortedSquares([-4,-1,0,3,10])
print(solution)