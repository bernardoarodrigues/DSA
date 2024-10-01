# Linear Search: loops through array's elements and checks if the value is found 
def linearSearch(list, value): # Time: O(n) - Space: O(1)
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1

def binarySearchHelper(list, l, r, value):
    if l < r:
        m = l + (r-l)//2
        
        if value == list[m]:
            return m
        elif value < list[m]:
            return binarySearchHelper(list, l, m-1, value)
        else:
            return binarySearchHelper(list, m+1, r, value)
    else:
        return -1
    
# Binary Search: gets middle element, checks if equal to target. If so, returns index. 
# Else, if <target, goes to left element, if >target, goes to the right.
# Obs.: requires ordered list
def binarySearch(list, value): # Time: O(logn) - Space: O(1)
    return binarySearchHelper(list, 0, len(list)-1, value)

list = [1,2,3,4,5]
#print(linearSearch(list, 10))
print(binarySearch(list, 0))

