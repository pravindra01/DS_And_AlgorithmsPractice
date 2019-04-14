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
        """
        Must initialize all items in class
        """
        self._dict = {}
        self.totalItemsInCache = 0
        self.maxCapacity = 0
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
        it call _dict get function to find if already present
        """
        item = self._dict.get(key)
        if(item == None):
            #add item to Cache
            item = DNode(key,value)
            self._addNode(item)
            self._dict[key]  = item
            self.totalItemsInCache += 1
            if self.totalItemsInCache > self.maxCapacity:
                self._removeLRUItemFromCache() 
        else:
            item.value = value
            self._moveToHead(item)
    
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
        del self._dict[item.key]
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
    ["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
    """
    cacheIns = LruCache(1)
    print "None"
    cacheIns.put(2,1)
    print "None"
    print cacheIns.get(2)
    cacheIns.put(3,2)
    print "None"
    print cacheIns.get(2)
    print cacheIns.get(3)
    # Your LRUCache object will be instantiated and called as such:
    command = ["LRUCache","put","put","get","put","put","get"]
    input = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    OUT= []
    for ind,com in enumerate(command):
        if com == "LRUCache":
            print("INIT************************** ", input[ind][0])
            A = LruCache(input[ind][0])
            OUT.append(None)
        elif com == "get":
            print "GET ************************** " , input[ind][0]
            OUT.append(A.get(input[ind][0]))
        else:
            print "PUT ************************** " , input[ind][0],input[ind][1]
            A.put(input[ind][0],input[ind][1] )
            OUT.append(None)
    print (OUT)