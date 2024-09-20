# lists in python (can store values of different data types)
print('---> lists in python')

# declaration + assignment
print('-> declaration + assignment')

integers = [1,2,3,4]
print(integers)
strings = ['milk', 'cheese', 'butter']
print(strings)
mixed = [1, 'two', 3.0, True]
print(mixed)
nested = [1, [2, 3], [4, [5, 6]]]
print(nested)
empty = []
print(empty)

print()

# access   
print('-> access')
print(integers[1])
print(integers[-1])   # returns last element
print(integers[-2])   # returns second last element
print(2 in integers)
print()

# traversal
print('-> traversal')
for i in integers:
    print(i, end=' ')
print()
for i in range(len(integers)):
    print(integers[i], end=' ')
print('\n')

# update 
print('-> update')
integers[3] = 1000
print(integers)
print()

# insertion
print('-> insertion')
integers.insert(0, 0)   # works with any index
integers.append(5)  # adds to the end of the list 
integers.extend([6, 7])
print(integers)
print()

# slice
print('-> slice')
print(integers[0:2])
print()

# deletion
print('-> deletion')
integers.pop(0)
integers.remove(7)
del integers[3:]
print(integers)
print()

# search
print('-> search')
# in operator   Time: O(n) for lists
target=3
if target in integers:
    print(f"{target} is in the list")
else: 
    print(f"{target} is not in the list")

# linear search 
def linearSearch(array, target):
    for i, value in enumerate(integers):
        if target == value:
            print(f"{target} is in the list at index {i}")
            return
    print(f"{target} is not in the list")
linearSearch(integers, 4)
print()

# list operations
print('-> list operations')

print('- concatenation')
a = [1,2,3]
b = [5,4,6]
c = a + b
print(a, ' + ', b, ' = ', c)
print()

print('- repeating elements')
d = [0]
d = d * 4
print(d)
print()

print('- max value element')
print(max(c))
print()

print('- min value element')
print(min(c))
print()

print('- sum of all elements')
print(sum(c))
print()

print('- sort')
print(sorted(c))
c.sort()
print(c)

# lists and strings
print('-> lists and strings')
print('- list(): gets list of characters')
e = 'string'
f = list(e) 
print(f, '\n')

print('- split(): splits string by delimiter')
e = 'word1 word2'
delimiter = 'd'
f = e.split(delimiter)   # default delimiter: ' '
print(f, '\n')

print('- join(): inverse of split()')
print(delimiter.join(f))
print()

# list comprehension   (works for list, range, string, tuple)
# new_list = [new_item for i in old_list] new_item is obtained in terms of i (item in old list)
print('-> list comprehension')
numbers = [-1,1,2,3,4,5]
doubledNumbers = [i*2 for i in numbers]
print(doubledNumbers)
word = 'python'
chars = [c for c in word]   # gets characters from string
print(chars)
print()

print('-> conditional list comprehension')
evenNumbers = [i for i in numbers if i % 2 == 0]
print(evenNumbers)
negativeNumbers = [i if i < 0 else 'positive' for i in numbers]
print(negativeNumbers)

import random
words = ['a', 'b', 'c']
random.shuffle(words)
print(words)

a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)