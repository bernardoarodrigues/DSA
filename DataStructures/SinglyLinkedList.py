# singly linked list in python (self.tail.next = None)
print('---> singly linked in python')

# Note: all of the following methods have a space complexity of O(1)

class Node:
    def __init__(self, value):   # Time: O(1)
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):   # Time: O(1)
        self.head = None
        self.tail = None    
        self.length = 0

    def __str__(self):   # Time: O(n)
        tempNode = self.head
        result = ''
        while tempNode:
            result += str(tempNode.value)
            if tempNode.next:
                result += ' -> '
            tempNode = tempNode.next
        return result

    def append(self, value):   # Time: O(1)
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1
    
    def prepend(self, value):   # Time: O(1)
        newNode = Node(value)
        if self.head == None:
            self.tail = newNode
        else:
            newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index, value):   # Time: O(n)
        newNode = Node(value)
        if index < 0 or index > self.length:
            print('error: index out of bounds')
            return
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            tempNode = self.head
            for _ in range(index-1):
                tempNode = tempNode.next
            newNode.next = tempNode.next
            tempNode.next = newNode
            if index == self.length:
                self.tail = newNode
        self.length += 1

    def traverse(self):   # Time: O(n)
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, value):   # Time: O(n)
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):   # Time: O(n)
        if index < 0 or index > self.length:
            print('error: index out of bounds')
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set(self, index, value):   # Time: O(n)
        tempNode = self.get(index)
        if tempNode:
            tempNode.value = value
            return True
        return False
    
    def popFirst(self):   # Time: O(1)
        if self.length == 0:
            print('error: empty list')
            return
        poppedNode = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            poppedNode.next = None
        self.length -= 1
        return poppedNode
    
    def pop(self):   # Time: O(n)
        if self.length == 0:
            print('error: empty list')
            return
        poppedNode = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return poppedNode

    def remove(self, index):   # Time: O(n)
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length-1 or index == -1:
            return self.pop()
        prevNode = self.get(index-1)
        poppedNode = prevNode.next
        prevNode.next = poppedNode.next
        poppedNode.next = None
        self.length -= 1
        return poppedNode
    
    def deleteAll(self):   # Time: O(1)  
        self.head = None
        self.tail = None
        self.length = 0
    
# declaration/assignment
linkedList = SinglyLinkedList()

# append
print('-> append')
linkedList.append(10)
linkedList.append(20)
print(linkedList, '\n')

# prepend
print('-> prepend')
linkedList.prepend(0)
print(linkedList, '\n')

# insert
print('-> insert')
linkedList.insert(0, -5)
linkedList.insert(3, 15)
linkedList.insert(5, 25)
print(linkedList, '\n')

# to string
print('-> to string')
print(linkedList, '\n')

# traverse
print('-> traverse')
linkedList.traverse()
print()

# search
print('-> search')
print('index of value 20: ' + str(linkedList.search(20)), '\n')

# get
print('-> get')
print('value at index 4: ' + str(linkedList.get(4).value), '\n')

# set
print('-> set')
linkedList.set(0, -10)
print(linkedList, '\n')

# popFirst
print('-> popFirst')
print(linkedList.popFirst().value)
print(linkedList, '\n')

# pop
print('-> pop')
print(linkedList.pop().value)
print(linkedList, '\n')

# remove
print('-> remove')
print(linkedList.remove(-1).value)
print(linkedList, '\n')

# delete all
print('-> delete all')
linkedList.deleteAll()
print(linkedList, '\n')