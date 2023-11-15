class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.length - 1:
            return -1
        p = self.head
        for _ in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            self.length += 1
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = ListNode(val)
        p = self.head
        for _ in range(index - 1):
            p = p.next
        new_node.next = p.next
        p.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        # 删除第一个节点
        if index == 0:
            p = self.head
            self.head = self.head.next
            p = None
            self.length -= 1
            return
        # 删除中间或末尾
        p = self.head
        pre = None
        for _ in range(index):
            pre = p
            p = p.next
        pre.next = p.next
        p = None
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
