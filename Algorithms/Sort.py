import math

# Stable: Bubble, Insertion, Bucket, Merge

# Bubble Sort: swap pairs if left > right, do it n*(n-i) times
# When to use: insufficient memory
def bubbleSort(list): # Time: O(n²) - Space: O(1)
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

# Selection Sort: get minValue and put in beginning repeatedly
# When to use: insufficient memory
def selectionSort(list): # Time: O(n²) - Space: O(1)
    for i in range(len(list)):
        minI = i
        for j in range(i+1, len(list)):
            if list[j] < list[minI]:
                minI = j
        list[i], list[minI] = list[minI], list[i]
    return list

# Insertion Sort: left to right, compare elements and put in correct place
# When to use: insufficient memory
def insertionSort(list): # Time: O(n²) - Space: O(1)
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
        print(list)
    return list 

# Bucket Sort: split list in buckets, sort each bucket, then merge them back
# When to use: when input is uniformly distributed, elements are close
def bucketSort(list): # Time: O(nlogn) - Space: O(n)
    bucketAmount = round(math.sqrt(len(list)))
    maxValue = max(list)
    arr = []
    
    for i in range(bucketAmount):
        arr.append([])
    
    for j in list:
        index_b = math.ceil(j*bucketAmount/maxValue)
        arr[index_b-1].append(j)
    
    for i in range(bucketAmount):
        arr[i] = quickSort(arr[i])

    k = 0 
    for i in range(bucketAmount):
        for j in range(len(arr[i])):
            list[k] = arr[j]
            k += 1

    return list

def merge(list, l, m, r): # Time: O(n) - Space: O(n)
    n1 = m-l+1; n2 = r-m
    L = [0]*n1; R = [0]*n2
    for i in range(n1):
        L[i] = list[l+i]
    for j in range(n2):
        R[j] = list [m+1+j]
    i = 0; j = 0; k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        list[k] = L[i]
        i += 1; k += 1
    while j < n2:
        list[k] = R[j]
        j += 1; k += 1
    return list

# Merge Sort: splits until separate units, then merges elements into ordered subsets, then repeats until everything is merged
# When to use: does stable sort, better time complexity than O(n²)
def mergeSort(list, l, r): # Time: O(nlogn) - Space: O(n)
    if l < r:
        m = (l+(r-1))//2
        mergeSort(list, l, m)
        mergeSort(list, m+1, r)
        merge(list, l, m, r)
    return list

def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

def pivot(list, pivot, end):
    swapIndex = pivot
    for i in range(pivot+1, end+1):
        if list[i] < list[pivot]:
            swapIndex += 1
            swap(list, swapIndex, i)
    swap(list, swapIndex, pivot)
    return swapIndex

def quickSortHelper(list, left, right):
    if left < right:
        pivotIndex = pivot(list, left, right)
        quickSortHelper(list, left, pivotIndex-1)
        quickSortHelper(list, pivotIndex+1, right)
    return list

# Quick Sort: recursive, based on 3 pointers: pivot, swap, index. every iteration: chooses a pivot (left-most element), 
# compares with other values, positions pivot in right place, and splits each side into smaller/larger elements. 
# Obs.: pivot selection is needed to ensure best time compl., otherwise it may lead to O(n²) time
def quickSort(list): # Time: O(nlogn) - Space: O(n) 
    return quickSortHelper(list, 0, len(list)-1)

def heapify(list, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and list[l] < list[smallest]:
        smallest = l
    if r < n and list[r] < list[smallest]:
        smallest = r
    
    if smallest != i:
        list[i], list[smallest] = list[smallest], list[i]
        heapify(list, n, smallest)

# Heap Sort: creates a heap tree with the array's elements, then extracts the root and turns the last node 
# into root (then balances again) recursively.
def heapSort(list): # Time: O(nlogn) - Space: O(1)
    n = len(list)
    for i in range(int(n/2)-1, -1, -1):
        heapify(list, n, i)
    
    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)
    list.reverse()
    return list

list = [7,6,5,4,8,9,1,0,2,3]
print(heapSort(list))
#print(mergeSort(list, 0, len(list)-1))