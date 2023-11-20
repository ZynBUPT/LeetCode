# 利用双向链表实现LRU缓存，其中靠近表头的结点为最近使用，靠近表尾的为最久未使用的
# 为了方便插入删除操作可以设置头结点与尾结点，减少判断
# 利用一个cache元组存放结点，以减少插入删除的空间复杂度
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.next = None
        self.pre = None
        self.value = value


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果存放有该关键字结点，移动到表头
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 从cache中取出该结点，读取数据后移动到表头
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
