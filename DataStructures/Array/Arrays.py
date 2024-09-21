# arrays in python (elements must have same data type)
print('---> arrays in python')
print('--> 1 dimension')

# declaration + assignment
print('-> declaration + assignment')

import array

myArray1 = array.array('i')             # Time & Space: O(1)
print(myArray1)
myArray2 = array.array('i', [1,2,3,4])  # Time & Space: O(n)
print(myArray2)
print()

import numpy as np

npArray1 = np.array([], dtype=int)          # Time & Space: O(1)
print(npArray1)
npArray2 = np.array([1,2,3,4], dtype=int)   # Time & Space: O(n)
print(npArray2)
print()

# insertion
print('-> insertion')
myArray2.insert(4, 5)       # Time: O(n)   Space: O(1)
print(myArray2)
print()

# access
print('-> access')
print(myArray2[0])          # Time: O(1)   Space: O(1)
print()

# traversal
print('-> traversal')
for i in myArray2:          # Time: O(n)   Space: O(1)
    print(i)
print()

# search
print('-> search')

def search(array, value):   # Time: O(n)   Space: O(1)
    for i in range(len(array)):          
        if array[i] == value:
            return i
    return -1

value = 3
print('position:', search(myArray2, value))
print()

# 2 dimensional arrays
print('--> 2 dimensions')

# declaration + assignment
print('-> declaration + assignment')

twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])   # Time: O(m*n)   Space: O(m*n) - m: rows n: cols
print(twoDArray)

# row insertion: axis=0
print('-> row insertion')
rowTwoDArray = np.insert(twoDArray, 0, [-2, -1, 0], 0)   # Time: O(m*n)   Space: O(j*k) - j: rows of subarray k: cols of subarray
print(rowTwoDArray)

# column insertion: axis=1
print('-> column insertion')
colTwoDArray = np.insert(twoDArray, 0, [0,0,0,0], 1)   # Time: O(m*n)   Space: O(j*k) - j: rows of subarray k: cols of subarray
print(colTwoDArray)

# note: append(array, subarray, axis) inserts subarray to the end of the array

# access
print('-> access')
print(twoDArray[0][2])          # Time: O(1)   Space: O(1)
print()

# traversal
print('-> traversal')   # Time: O(m*n)   Space: O(1)
for row in range(len(twoDArray)):          
    for col in range(len(twoDArray[row])):
        print(twoDArray[row][col], end=' ')
print()

# search
print('-> search')   
def linearSearch(array, value):   # Time: O(m*n)   Space: O(1)
    print('the value ' + str(value) + ' ', end='')
    for row in range(len(twoDArray)):          
        for col in range(len(twoDArray[row])):
            if(twoDArray[row][col] == value):
                print('is located at index: ' + str(row) + ';' + str(col))
                return
    print('is not in the array')

linearSearch(twoDArray, 10)

# row deletion: axis=0
print('-> row deletion')   
delRowTwoDArray = np.delete(twoDArray, 2, 0)   # Time: O(m*n)   Space: O(m*n)
print(delRowTwoDArray)

# column deletion: axis=0
print('-> column deletion')   
delColTwoDArray = np.delete(twoDArray, 2, 1)   # Time: O(m*n)   Space: O(m*n)
print(delColTwoDArray)

