
nodeCount = 0

class Node:

    count = 0

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        Node.count += 1
        
    def initSeq(self, n):
        if n <= Node.count:
            return

        y = 2 * self.value + 1
        z = 3 * self.value + 1

        self.left = Node(y)
        self.right = Node(z)
        
        self.left.initSeq(n)
        self.right.initSeq(n)
    
    def values(self, acc=[]):
        if self.value not in acc:
          acc.append(self.value)

        if self.left is not None:
            self.left.values(acc)
        
        if self.right is not None:
            self.right.values(acc)
        
        acc.sort()
        return acc
        
tree = Node(1)
tree.initSeq(999)
sequence = tree.values()

def dbl_linear(n):
    print(n)
    if n == 0:
        return 1
    
    print(sequence[:n])
    [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
    return sequence[n + 1]
    
    
    
    
    
        