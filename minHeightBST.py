
def minHeightBSTHelper(array):
    return minHeightBST(array, BST(None))


# array, BST, startIdx, endIdx
# [ 1, 2, 5, 7, 10, 13, 14, 15, 22]

# insert middleIdx value to BST
# recursivly call minHeightBSTHelper(array, BST, startIdx, midIdx - 1)
# recursivly call minHeightBstHelper(array, BST, midIdx, endIdx)

def minHeightBST(array):
    return minHeightBSTHelper(array, 0, len(array) - 1)

# get middleIdx
# get middleValue
# create BST with middle value
# create BST.left with left array
# create BST.right with right array


def minHeightBSTHelper(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None

    middleIdx = (startIdx + endIdx) // 2
    bst = BST(array[middleIdx])

    bst.left = minHeightBSTHelper(array, startIdx, middleIdx - 1)
    bst.right = minHeightBSTHelper(array, middleIdx + 1, endIdx)

    return bst


def printBST(bst):
    if bst is None:
        return

    printBST(bst.left)
    print(bst.value)
    printBST(bst.right)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


bst = minHeightBST([1, 2, 5, 7, 10, 13, 14, 15, 22])
printBST(bst)
