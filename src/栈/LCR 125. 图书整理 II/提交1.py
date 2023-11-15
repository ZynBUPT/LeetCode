class CQueue:
    # 双栈实现一个队列
    # A、B两个书车视为2个栈
    def __init__(self):
        # 初始化为空
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        # 还书直接放到A车顶部
        self.A.append(value)

    # 借书
    def deleteHead(self) -> int:
        # 如果B车有，把B顶部的输出，因为B顶部是A的栈底，即最早归还的书
        if self.B:
            return self.B.pop()
        # 如果两车都没书，返回-1
        if not self.A:
            return -1
        # 只有A有书，把A弹出到B，返回B顶部的书
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
