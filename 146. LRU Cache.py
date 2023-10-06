class DlinkedNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
class LRUCache:
    def _remove_node(self, node): #找到当前node的prev和next进行删除/改变指向
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _add_node(self,node): #最近使用过的加在head后面
        node.prev = self.head
        node.next = self.head.next
        

        self.head.next.prev = node
        self.head.next = node

    def _pop_tail(self): #找到tail之前的node  删除掉
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DlinkedNode(), DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._remove_node(node) #新加入的值，要把它加在离head最近的的地方，因为得知道谁最近被使用过，容量不够的时候要删除
        self._add_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            newNode = DlinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size +=1

            if self.size > self.capacity:
                tail = self._pop_tail()#删除掉 没有最近使用的node  也就是tail之前的node
                del self.cache[tail.key] #{}中也得删除
                self.size -= 1
        else:
            node.value = value
            self._remove_node(node)
            self._add_node(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)