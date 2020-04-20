

def find_word(board, word):
    height = len(board)
    width = len(board[0])
    
    for row in range(height):
        for col in range(width):
            if dfs(board, row, col, word):
                return True
    
    return False


def dfs(board, row, col, word):

    height = len(board)
    width = len(board[0])

    if len(word) == 0:
        return True

    if row < 0 or col < 0 or row >= height or col >= height or board[row][col] != word[0]:
        return False

    board[row][col] = '#'
    neighborDirections = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for rowOffset, colOffset in neighborDirections:
        if dfs(board, row + rowOffset, col + colOffset, word[1:]):
            return True

    board[row][col] = word[0]
    
    return False

testBoard = [
    ["E","A","R","A"],
    ["N","L","E","C"],
    ["I","A","I","S"],
    ["B","Y","O","R"]
]

find_word(textBoard, "CEREAL")