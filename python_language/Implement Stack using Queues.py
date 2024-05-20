# Stack Implementation using linkedList
class node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
class MyStack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        nn = node(x)
        nn.next = self.head
        self.head = nn
        

    def pop(self) -> int:
        temp = self.head.val
        self.head = self.head.next
        return temp

    def top(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        return not self.head


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
