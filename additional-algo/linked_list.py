class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

        return self

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        else:
            curNode = self.head
            for _ in range(index):
                curNode = curNode.next
            return curNode

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            poppedNode = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return poppedNode
        else:
            poppedNode = self.tail
            newTail = self.get(self.length - 2)
            newTail.next = None
            self.tail = newTail
            self.length -= 1
            return poppedNode

    def shift(self, val):
        newNode = Node(val)
        old_head = self.head
        self.head = newNode
        self.head.next = old_head
        if self.length == 0:
            self.tail = newNode
        self.length += 1
        return self

    def unshift(self):
        if self.length == 0:
            return None
        else:
            unshifted_node = self.head
            self.head = self.head.next
            unshifted_node.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return unshifted_node

    def set(self, index, val):
        if index >= self.length or index < 0:
            return None
        else:
            curNode = self.get(index)
            curNode.val = val
            return curNode.val

    def insert(self, index, val):
        if index == self.length:
            self.push(val)
        elif index == 0:
            self.shift(val)
        elif index < 0 or index > self.length:
            return None
        else:
            newNode = Node(val)
            prevNode = self.get(index - 1)
            nextNode = self.get(index)
            prevNode.next = newNode
            newNode.next = nextNode
            self.length += 1
            return self

    def remove(self, index):
        if index == 0:
            return self.unshift()
        elif index == self.length - 1:
            return self.pop()
        elif index < 0 or index >= self.length:
            return None
        else:
            removeNode = self.get(index)
            prevNode = self.get(index - 1)
            nextNode = self.get(index + 1)
            prevNode.next = nextNode
            removeNode.next = None
            self.length -= 1
            return removeNode

    def reverse(self):
        curNode = self.head
        prevNode = None
        # swap head and tail
        curHead = self.head
        self.head = self.tail
        self.tail = curHead
        while curNode is not None:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        return self.display()


list = LinkedList()

list.push(10)
list.push(4)
list.push(18)
list.push(23)
list.display()
print(list.reverse())
list.display()