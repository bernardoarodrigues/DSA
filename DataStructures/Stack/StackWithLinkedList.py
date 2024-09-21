# stack (last in first out - LIFO)
print('---> stack')

# Note: all of the following methods have a space complexity of O(1)

class Node:
    def __init__(self, value):   # Time: O(1)
        self.value = value
        self.next = None

class Stack: 
    def __init__(self):   # Time: O(1)
        self.head = None

    def __str__(self):   # Time: O(n)
        result = ''
        node = self.head
        while node:
            result += str(node.value)
            node = node.next
            if node:
                result += '\n'
        return result

    def isEmpty(self):   # Time: O(1)
        return self.head is None
    
    def push(self, value):   # Time: O(1)
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    def pop(self):   # Time: O(1)
        if self.isEmpty():
            print('stack is empty')
            return
        nodeVal = self.head.value
        self.head = self.head.next
        return nodeVal
    
    def peek(self):   # Time: O(1)
        if self.isEmpty():
            print('stack is empty')
            return
        return self.head.value
    
    def delete(self):   # Time: O(1)
        self.head = None

# declaration/assignment
stack = Stack()

# push
print('-> push')
stack.push(1)
stack.push(2)
stack.push(3)
print(stack, '\n')

# pop
print('-> pop')
print('removed:', stack.pop())
print(stack, '\n')

# peek
print('-> peek')
print(stack.peek(), '\n')

# delete
print('-> delete')
stack.delete()
print(stack)
