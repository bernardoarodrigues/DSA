# circular singly linked list in python (self.tail.next = self.head)
print('---> circular singly linked in python')

# Note: all of the following methods have a space complexity of O(1)

class Node:
    def __init__(self, value):   # Time: O(1)
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):   # Time: O(1)
        self.head = None
        self.tail = None    
        self.length = 0
    
    def __str__(self):   # Time: O(n)
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += ' -> '
        return result
    
    def append(self, value):   # Time: O(1)
        newNode = Node(value)
        if self.length == 0:
            self.head = self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode
        self.length += 1

    def prepend(self, value):   # Time: O(1)
        newNode = Node(value)
        if self.length == 0:
            self.head = self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        self.length += 1

    def insert(self, index, value):   # Time: O(n)
        if index == 0 or self.length == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        elif index < 0 or index > self.length:
            raise Exception('index out of range')
        else:
            newNode = Node(value)
            prevNode = self.head
            for _ in range(index-1):
                prevNode = prevNode.next
            newNode.next = prevNode.next
            prevNode.next = newNode
            self.length += 1

    def traverse(self):   # Time: O(n)
        node = self.head
        for _ in range(self.length):
            print(node.value)
            node = node.next  
            
    def search(self, value):   # Time: O(n)
        node = self.head
        for index in range(self.length):
            if node.value == value:
                return index
            node = node.next  
        return -1

    def get(self, index):   # Time: O(n)
        if index < -1 or index > self.length:
            raise Exception('index out of range')
        elif index == -1:
            return self.tail
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set(self, index, value):   # Time: O(n)
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def popFirst(self):   # Time: O(1)
        if self.length == 0:
            return None
        newNode = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            newNode.next = None
        self.length -= 1
        return newNode
    
    def pop(self):   # Time: O(n)
        if self.length == 0:
            return None
        poppedNode = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            prevNode = self.get(self.length-2)
            prevNode.next = self.head
            self.tail = prevNode
            poppedNode.next = None
        self.length -= 1
        return poppedNode

    def remove(self, index):   # Time: O(n)
        if self.length == 0 or index < -1 or index >= self.length:
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
    
    def deleteAll(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = self.tail = None
        self.length = 0
    

# declaration/assignment
linkedList = CircularSinglyLinkedList()

# append
print('-> append')
linkedList.append(10)
linkedList.append(20)
linkedList.append(30)
print(linkedList, '\n')

# prepend
print('-> prepend')
linkedList.prepend(0)
print(linkedList, '\n')

# insert
print('-> insert')
linkedList.insert(3, 25)
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
print('value at index 4: ' + str(linkedList.get(-1).value), '\n')

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