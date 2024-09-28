# Binary Heap is a complete binary tree: every level of the tree is completely filled except for the last level.
# All the nodes are as left as possible.
# Two types:
# 1. Max-Heap: value of any node should be greater than its child nodes.
# 2. Min-Heap: value of any node should be less than its child nodes.

class Heap:
    def __init__(self, size): # Time: O(1) - Space: O(n)
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size+1

def peek(root): # Time: O(1) - Space: O(1)
    if not root:
        return
    return root.customList[1]

def size(root): # Time: O(1) - Space: O(1)
    if not root:
        return
    return root.heapSize

def levelOrderTraversal(root): # Time: O(n) - Space: O(1)
    if not root:
        return 
    for i in range(1, root.heapSize+1):
        print(root.customList[i])

def heapifyTreeInsert(rootNode, index, heapType): # Time: O(logN) - Space: O(logN)
    parentIndex = int(index / 2)
    if parentIndex < 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
            
def insertNode(rootNode, value, heapType): # Time: O(logN) - Space: O(logN)
    if rootNode.heapSize+1 == rootNode.maxSize:
        return "The binary heap is full"
    rootNode.customList[rootNode.heapSize+1] = value
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

def heapifyTreeExtract(rootNode, index, heapType): # Time: O(logN) - Space: O(logN)
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)

def extract(rootNode, heapType): # Time: O(logn) - Space: O(logn)
    if rootNode.heapSize == 0:
        return
    extractedNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractedNode

def delete(rootNode): # Time: O(1) - Space: O(1)
    rootNode.heapSize = 0
    rootNode.customList = None
    return "Success"

binaryHeap = Heap(5)
print(insertNode(binaryHeap, 4, "Max"))
print(insertNode(binaryHeap, 5, "Max"))
print(insertNode(binaryHeap, 2, "Max"))
print(insertNode(binaryHeap, 1, "Max"))
extract(binaryHeap, "Max")
delete(binaryHeap)
levelOrderTraversal(binaryHeap)
