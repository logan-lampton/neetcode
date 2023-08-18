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


list = LinkedList()

list.push(10)

print(list.unshift().val)
list.display()