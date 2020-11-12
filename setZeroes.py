class Solution(object):
    
    def dfsIncreaseRow(self, matrix, row, col):
        
        if row >= len(matrix):
            return
        
        if matrix[row][col] != 0:
            matrix[row][col] = '#'
        
        self.dfsIncreaseRow(matrix, row + 1, col)
    
    def dfsDecreaseRow(self, matrix, row, col):
        
        if row < 0:
            return
        
        if matrix[row][col] != 0:
            matrix[row][col] = '#'
        
        self.dfsDecreaseRow(matrix, row - 1, col)
    
    def dfsIncreaseCol(self, matrix, row, col):
        
        if col >= len(matrix[0]):
            return
        
        if matrix[row][col] != 0:
            matrix[row][col] = '#'
        
        self.dfsIncreaseCol(matrix, row, col + 1)
    
    def dfsDecreaseCol(self, matrix, row, col):
        
        if col < 0:
            return

        if matrix[row][col] != 0:
            matrix[row][col] = '#'
        
        self.dfsDecreaseCol(matrix, row, col - 1)
        
    
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.dfsIncreaseRow(matrix, i, j)
                    self.dfsDecreaseRow(matrix, i, j)
                    self.dfsIncreaseCol(matrix, i, j)
                    self.dfsDecreaseCol(matrix, i, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
        
        return matrix
                    
        
