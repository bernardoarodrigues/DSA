# queue (first in first out - FIFO)
print('---> queue')

class Queue: 
    def __init__(self):   # Time: O(1)
        self.list = []

    def __str__(self):   # Time: O(n)   Space: O(1)
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    def isEmpty(self):   # Time: O(1)   Space: O(1)
        if self.list == []:
            return True
        return False
    
    def enqueue(self, value):   # Time: amortized O(1)   Space: O(1)
        self.items.append(value)
    
    def dequeue(self):   # Time: O(n)   Space: O(1)
        if self.isEmpty():
            print('queue is empty')
            return
        return self.items.pop(0)
    
    def peek(self):   # Time: O(1)   Space: O(1)
        if self.isEmpty():
            print('stack is empty')
            return
        return self.list[0]
    
    def delete(self):   # Time: O(1)   Space: O(1)
        self.list = []

# declaration/assignment
queue = Queue()

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
