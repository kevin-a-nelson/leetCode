class Node:
    """node of doubly-linked list"""
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        

class LRUCache:
    """data structure
    hashtable mapping key to (key-val) node
    doubly linked list to keep order 
    """
    def __init__(self, capacity: int):
        self.cpty = capacity
        self.dict = dict() #hash table
        self.head, self.tail = Node(), Node() #doubly-linked list 
        self.head.next = self.tail
        self.tail.prev = self.head 

    def _remove(self, node):
        """remove node from dll"""
        node.next.prev = node.prev
        node.prev.next = node.next 

    def _append(self, node):
        """append node at tail"""
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        """return value corresponding to key"""
        if key not in self.dict: return -1
        #update its order to most recent
        node = self.dict[key]
        self._remove(node)
        self._append(node)
        return self.dict[key].val
    
    def put(self, key: int, value: int) -> None:
        """insert key-value pair into cache"""
        if key not in self.dict: 
            node = Node(key, value)
            self.dict[key] = node
        else:
            #if exists, update value & switch to end
            node = self.dict[key]
            node.val = value 
            self._remove(node) #remove node from dll
        self._append(node) #append node at tail
        
        #exceeding capacity
        if len(self.dict) > self.cpty:
            #remove from dict
            key = self.head.next.key
            node = self.dict[key] #least recent 
            self.dict.pop(key)    #remove from dict
            self._remove(node)    #remove from dll