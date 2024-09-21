# stack (last in first out - LIFO)
print('---> stack')

# Note: all of the following methods have a space complexity of O(1)

class Stack: 
    def __init__(self):   # Time: O(1)
        self.list = []

    def __str__(self):   # Time: O(n)
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):   # Time: O(1)
        return self.list == []
    
    def push(self, value):   # Time: O(1) amortized, bc if it has to reallocate memory, it'll be O(n²)
        self.list.append(value)
    
    def pop(self):   # Time: O(1)
        if self.isEmpty():
            print('stack is empty')
            return
        return self.list.pop()
    
    def peek(self):   # Time: O(1)
        if self.isEmpty():
            print('stack is empty')
            return
        return self.list[-1]
    
    def delete(self):   # Time: O(1)
        self.list = []

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
stack.pop()
print(stack, '\n')

# peek
print('-> peek')
print(stack.peek(), '\n')

# delete
print('-> delete')
stack.delete()
print(stack)
