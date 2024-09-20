# doubly linked list in python (next and prev node references)
print('---> doubly linked in python')

# Note: all of the following methods have a space complexity of O(1)

class Node:
    def __init__(self, value):   # Time: O(1)
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)

class DoublyLinkedList:
    def __init__(self) -> None:   # Time: O(1)
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):   # Time: O(n)
        tempNode = self.head
        result = ''
        while tempNode:
            result += str(tempNode.value)
            if tempNode.next:
                result += ' <-> '
            tempNode = tempNode.next
        return result
    
    def append(self, value):   # Time: O(1)
        newNode = Node(value)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
    
    def prepend(self, value):   # Time: O(1)
        newNode = Node(value)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def traverse(self):   # Time: O(n)
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def reverse(self):   # Time: O(n)
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
    
    def search(self, value):   # Time: O(n)
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, index):   # Time: O(n/2) => O(n)   (because we remove the constants)
        if index < 0 or index >= self.length:
            raise Exception('index out of bounds')

        if index < self.length // 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length-1, index, -1):
                node = node.prev
        return node

    def set(self, index, value):   # Time: O(n)
        node = self.get(index)
        node.value = value

    def insert(self, index, value):   # Time: O(n)
        if index < 0 or index > self.length:
            raise Exception('index out of bounds')

        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return

        newNode = Node(value)
        prevNode = self.get(index-1)
        newNode.next = prevNode.next
        newNode.prev = prevNode
        prevNode.next.prev = newNode
        prevNode.next = newNode
        self.length += 1

    def popFirst(self):   # Time: O(1)
        if self.length == 0:
            return None
        node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        self.length -= 1
        return node

    def pop(self):   # Time: O(1)
        if self.length == 0:
            return None
        node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None
        self.length -= 1
        return node
    
    def remove(self, index):   # Time: O(n)
        if index == 0:
            return self.popFirst()
        elif index == self.length-1:
            return self.pop()
        elif index < 0 or index >= self.length:
            return None
        
        node = self.get(index)
        if self.length == 1:
            self.head = self.tail = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None
        self.length -= 1
        return node
    
    def deleteAll(self):
        self.head = self.tail = None
        self.length = 0
        
# declaration/assignment
linkedList = DoublyLinkedList()

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

# reverse
print('-> reverse')
linkedList.reverse()
print()

# search
print('-> search')
print('index of value 20: ' + str(linkedList.search(20)), '\n')

# get
print('-> get')
print('value at index 3: ' + str(linkedList.get(3).value), '\n')

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

# deleteAll
print('-> deleteAll')
linkedList.deleteAll()
print(linkedList)