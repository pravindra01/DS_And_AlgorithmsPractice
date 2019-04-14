# Create LRU Cache with python
# implemented using Double linked list and python dictionary

class DNode:
    prev = None
    next = None

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LruCache:
    _dict = {}
    totalItemsInCache = 0
    maxCapacity = 0
    head = None
    tail = None

    def __init__(self,maxSize):
        self.maxCapacity = maxSize
        self.head = DNode(None,None)
        self.tail = DNode(None,None)
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None

    def put(self,key,value):
        """
        adds a item to cache if not already present
        it call get function that will take care of moving object to front of list if already present
        """
        item = self.get(key)
        if(item == -1):
            #add item to Cache
            item = DNode(key,value)
            self._addNode(item)
            self._dict[key]  = item
            self.totalItemsInCache += 1
            if self.totalItemsInCache > self.maxCapacity:
                self._removeLRUItemFromCache()          
    
    def get(self,key):
        """
        retrive item from hashtable and move it to head
        otherwise return -1
        """
        item = self._dict.get(key)
        if(item == None):
            return -1
        self._moveToHead(item)
        return item.value

    def _removeLRUItemFromCache(self):
        """
        remove item from linked list and hash table
        """
        item = self._removeLastItemfromLList()
        self._dict.pop(item.key)
        self.totalItemsInCache -=1
    
    def _removeNode(self, node):
        """
        remove node from linked list
        """
        nextNode = node.next
        prevNode = node.prev
        # remove Node
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def _addNode(self, node):
        """
        add it head, to maintain LRU
        """
        headnext = self.head.next
        node.next = headnext
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _moveToHead(self, node):
        """
        move to head of linked list
        """
        self._removeNode(node)
        self._addNode(node)

    def _removeLastItemfromLList(self):
        """
        remove from tail
        """
        itemtoRemove = self.tail.prev
        self._removeNode(itemtoRemove)
        return itemtoRemove
        

if __name__ == "__main__":
    """
    Simple tests to demonstrate LRU Cache
    """
    cacheIns = LruCache(2)
    cacheIns.put(5,5)
    cacheIns.put(10,10)
    cacheIns.put(20,20)
    print cacheIns.get(10)
    print cacheIns.get(5)
    print cacheIns.get(4)
    print cacheIns.get(20)