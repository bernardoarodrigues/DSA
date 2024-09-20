from multiprocessing import Queue

# declaration/assignment
queue = Queue(3)

# enqueue
queue.put(1)
queue.put(2)
queue.put(3)

print('isFull:', queue.full()) # isFull
print('first element:', queue.get()) # pop
print('size:', queue.qsize()) # element count 