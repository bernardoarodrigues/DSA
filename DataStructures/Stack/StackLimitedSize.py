# stack (with limited size)
print('---> stack with limited size')

# Note: all of the following methods have a space complexity of O(1)

class StackLimitedSize: 
    def __init__(self, maxSize):   # Time: O(1)
        self.list = []
        self.maxSize = maxSize

    def __str__(self):   # Time: O(n)
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):   # Time: O(1)
        return self.list == []
    
    def isFull(self):
        return len(self.list) == self.maxSize
    
    def push(self, value):   # Time: O(1) amortized, bc if it has to reallocate memory, it'll be O(n²)
        if(self.isFull):
            print('stack is full')
            return
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
stack = StackLimitedSize(3)

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
