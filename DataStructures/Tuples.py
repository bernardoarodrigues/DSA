# tuples in python (immutable/hashable/comparable lists)
print('---> tuples in python')

# declaration + assignment   O(n)
print('-> declaration + assignment')
myTuple = (1,2,3,4,5)
print(myTuple)
oneEl = (1,)
print(oneEl)
myTuple2 = tuple()
print(myTuple2) 
myTuple2 += (2,)
print(myTuple2)

# access   O(1)
print(' -> access')
print(myTuple[0])
print(myTuple[-1])

# slice   O(n)
print(' -> slice')
print(myTuple[1:3])
print(myTuple[:3])

# traversal   O(n)
print(' -> traversal')
for i in myTuple:
    print(i)
print()

for i in range(len(myTuple)):
    print(f'index: {i} value: {myTuple[i]}')

# search   O(n)
value = 3

print(myTuple.index(value))

def tupleSearch(tuple, value):
    for i in range(len(tuple)):
        if myTuple[i] == value:
            return i
    return -1
print(tupleSearch(myTuple, value))

# operations
print(' -> operations')
t1 = (1,2,3)
t2 = (3,4,5)
print(t1+t2)
print(t1*4)
print(4 in t1)
print(t1.count(1))
print(t1.index(3))
print(len(t1))
print(max(t1))
print(tuple([1,2,3]))

tl = ([1,2],)
tl[0][1]=3
print(tl)

init_tuple = ()
print (init_tuple.__len__())