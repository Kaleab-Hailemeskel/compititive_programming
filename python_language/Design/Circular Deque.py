# I want to try this code with only one head, used as a linker 
# between the first and last node instead of holding reference to their values. 
# In that case there won't be tail Only head

class Deque:
    def __init__(self, val :int):
        self.val = val
        self.next = None
        self.previous = None

class MyCircularDeque:

    def __init__(self, val: int):
        self.maxSize = val
        self.currSize = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.currSize >= self.maxSize:
            return False
        newNode = Deque(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
        self.currSize += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.currSize >= self.maxSize:
            return False
        newNode = Deque(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.currSize += 1
        return True

    def deleteFront(self) -> bool:
        if not self.currSize:
            return False
        if self.currSize  == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prevoius = None
            del temp
        self.currSize -= 1
        return True
    
    def deleteLast(self) -> bool:
        if not self.currSize:
            return False
        if self.currSize == 1:
            self.head = self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None
        
            del temp
        self.currSize -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if self.currSize else -1
           
    def getRear(self) -> int:
        return self.tail.val if self.currSize else - 1

    def isEmpty(self) -> bool:
        return False if self.currSize else True

    def isFull(self) -> bool:
        return True if self.currSize == self.maxSize else False
