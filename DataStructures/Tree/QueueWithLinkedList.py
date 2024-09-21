# queue (with linked list)
# Note: all of the following methods have a space complexity of O(1)

class Node:
    def __init__(self, value):    # Time: O(1)
        self.value = value
        self.next = None

class LinkedList:   # Time: O(1)
    def __init__(self):
        self.head = self.tail = None
    
    def __iter__(self):   # Time: O(n)
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue: 
    def __init__(self):   # Time: O(1)
        self.linkedList = LinkedList()

    def __str__(self):   # Time: O(n)
        values = [str(x.value) for x in self.linkedList]
        return ' '.join(values)
    
    def isEmpty(self):   # Time: O(1)
        return self.linkedList.head == None
    
    def enqueue(self, value):   # Time: O(1)
        newNode = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def dequeue(self):   # Time: O(1)
        if self.isEmpty():
            print('queue is empty')
            return
        node = self.linkedList.head
        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head = self.linkedList.tail = None
        else:
            self.linkedList.head = node.next
            node.next = None
        return node
    
    def peek(self):   # Time: O(1)
        if self.isEmpty():
            print('stack is empty')
            return
        return self.linkedList.head.value
    
    def delete(self):   # Time: O(1) 
        self.linkedList.head = self.linkedList.tail = None