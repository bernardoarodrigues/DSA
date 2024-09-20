from collections import deque

# declaration/assignment
queue = deque(maxlen=3)

# enqueue
print('-> enqueue')
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue, '\n')

# dequeue
print('-> dequeue')
print('removed:', queue.popleft())
print(queue, '\n')

# delete
print('-> delete')
queue.clear()
print(queue)