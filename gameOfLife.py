class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        LIVING_CELL = 1
        DEAD_CELL = 0
        
        height = len(board)
        width = len(board[0])
        
        cellCords = []
        
        directions = [
            (1, 0), (-1, 0), 
            (0, 1), (0, -1), 
            (1, 1), (1, -1), 
            (-1, 1), (-1, -1)
        ]
        
        for boardX in range(height):
            for boardY in range(width):
                neighbors = 0
                for dirX, dirY in directions:

                    x = boardX + dirX
                    y = boardY + dirY
                    
                    if x >= height or x < 0 or y >= width or y < 0:
                        continue
                    
                    if board[x][y] == LIVING_CELL:
                        neighbors += 1
                
                cellCords.append((boardX, boardY, neighbors))
                
        print(cellCords)
        
        for cellX, cellY, neighbors in cellCords:
            if board[cellX][cellY] == LIVING_CELL:
                if neighbors < 2 or neighbors > 3:
                    board[cellX][cellY] = DEAD_CELL
            else:
                if neighbors == 3:
                    board[cellX][cellY] = LIVING_CELL
        