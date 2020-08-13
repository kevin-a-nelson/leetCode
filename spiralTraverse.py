def spiralTraverse(array):
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if(startRow > endRow):
        return

    if(startCol > endCol):
        return

    for col in range(startCol + 1, endCol + 1):
        result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    spiralFill(array, startRow + 1, endRow - 1,
               startCol + 1, endCol - 1, result)
