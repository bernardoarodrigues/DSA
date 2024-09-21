# queue (with max size)
print('---> queue with max size')

class Queue: 
    def __init__(self, maxSize):   # Time: O(1)   Space: O(n)
        self.list = maxSize * [None]
        self.maxSize = maxSize
        self.start = self.top = -1

    def __str__(self):   # Time: O(n)   Space: O(1)
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    def isFull(self):   # Time: O(1)   Space: O(1)
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        return False
    
    def isEmpty(self):   # Time: O(1)   Space: O(1)
        if self.top == -1:
            return True
        return False
    
    def enqueue(self, value):   # Time: O(1)   Space: O(1)
        if self.isFull():
            print('queue is full')
            return
        if self.top + 1 == self.maxSize:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
            self.list[self.top] = value
    
    def dequeue(self):   # Time: O(1)   Space: O(1)
        if self.isEmpty():
            print('queue is empty')
            return
        element = self.list[self.start]
        self.list[self.start] = None
        if self.start == self.top:
            self.start = self.top = -1
        elif self.start + 1 == self.maxSize:
            self.start = 0
        else:
            self.start += 1
        return element
    
    def peek(self):   # Time: O(1)   Space: O(1)
        if self.isEmpty():
            print('stack is empty')
            return
        return self.list[self.start]
    
    def delete(self):   # Time: O(1)   Space: O(1)
        self.list = self.maxSize * [None]
        self.start = self.top = -1

# declaration/assignment
queue = Queue(3)

# enqueue
print('-> enqueue')
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue, '\n')

# dequeue
print('-> dequeue')
print('removed:', queue.dequeue())
print(queue, '\n')

# peek
print('-> peek')
print(queue.peek(), '\n')

# delete
print('-> delete')
queue.delete()
print(queue)
