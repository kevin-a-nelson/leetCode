class Solution:
        
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0:
            return matrix
        
        if len(matrix[0]) == 0:
            return matrix
        
        if len(matrix) == 1:
            return matrix[0]
        
        row = 0
        col = 0
        
        VISITED = '*'
        
        spiral = []
        
        COLS = len(matrix[0])
        ROWS = len(matrix)
        
        while len(spiral) < COLS * ROWS:
            
            while col < COLS and matrix[row][col] != VISITED:
                
                spiral.append(matrix[row][col])
                matrix[row][col] = VISITED
                col += 1
            
            col -= 1
            row += 1
            
            while row < ROWS and matrix[row][col] != VISITED:
                
                spiral.append(matrix[row][col])
                matrix[row][col] = VISITED
                row += 1
                
            row -= 1
            col -= 1
            
            while col >= 0 and matrix[row][col] != VISITED:
                
                spiral.append(matrix[row][col])
                matrix[row][col] = VISITED
                col -= 1
            
            col += 1
            row -= 1
            
            while row >= 0 and matrix[row][col] != VISITED:
                
                spiral.append(matrix[row][col])
                matrix[row][col] = VISITED
                row -= 1
            
            row += 1
            col += 1
                
        return spiral
                
            
            
            
            