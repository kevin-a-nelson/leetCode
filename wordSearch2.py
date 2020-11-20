class Solution:

    # Loop through grid
    # dfs each cell
    # keep a visited hash


    def exist(self, board, word):

        visited = {}

        for rowIdx, row in enumerate(board):
            for colIdx, col in enumerate(board[0]):
                if self.getWord(board, word, rowIdx, colIdx, visited):
                    return True
        return False
    
    def getWord(self, board, word, rowIdx, colIdx, visited, wordIdx = 0):

        minRowIdx = 0
        maxRowIdx = len(board) - 1

        minColIdx = 0
        maxColIdx = len(board[0]) - 1

        if wordIdx == len(word):
            return True

        if rowIdx < minRowIdx or rowIdx > maxRowIdx:
            return False
        
        if colIdx < minColIdx or colIdx > maxColIdx:
            return False
        
        if visited.get((rowIdx, colIdx)):
            return False
        
        if board[rowIdx][colIdx] != word[wordIdx]:
            return False
        
        visited[(rowIdx, colIdx)] = True

        word = self.getWord(board, word, rowIdx, colIdx + 1, visited, wordIdx + 1) \
            or self.getWord(board, word, rowIdx, colIdx - 1, visited, wordIdx + 1) \
            or self.getWord(board, word, rowIdx + 1, colIdx, visited, wordIdx + 1) \
            or self.getWord(board, word, rowIdx - 1, colIdx, visited, wordIdx + 1)

        visited[(rowIdx, colIdx)] = False

        return word


board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
solution = Solution().exist(board, word)

print(solution)