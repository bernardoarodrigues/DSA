# binary search tree (with linked list)

import QueueWithLinkedList

class BSTNode:
    def __init__(self, data=None): # Time: O(1) - Space: O(1)
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(root, value): # Time: O(logn) - Space: O(logn)
    if root.data is None:
        root.data = value
    elif value <= root.data:
        if root.leftChild is None:
            root.leftChild = BSTNode(value)
        else:
            insertNode(root.leftChild, value)
    else:
        if root.rightChild is None:
            root.rightChild = BSTNode(value)
        else:
            insertNode(root.rightChild, value)
    return "Success"

def preOrderTraversal(node): # Time: O(n) - Space: O(n)
    if not node:
        return
    print(node.data)
    preOrderTraversal(node.leftChild)
    preOrderTraversal(node.rightChild)

def inOrderTraversal(node): # Time: O(n) - Space: O(n)
    if not node:
        return
    inOrderTraversal(node.leftChild)
    print(node.data)
    inOrderTraversal(node.rightChild)

def postOrderTraversal(node): # Time: O(n) - Space: O(n)
    if not node:
        return
    postOrderTraversal(node.leftChild)
    postOrderTraversal(node.rightChild)
    print(node.data) 

def levelOrderTraversal(node): # Time: O(n) - Space: O(n)
    if not node:
        return
    customQueue = QueueWithLinkedList.Queue()
    customQueue.enqueue(node)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)

def search(root, value): # Time: O(logn) - Space: O(logn)
    if root.data == value:
        return "Success"
    elif value <= root.data:
        if root.leftChild:
            return search(root.leftChild, value)
    else:
        if root.rightChild:
            return search(root.rightChild, value)
    return "Node not found"

def minValueNode(root): # Time: O(logn) - Space: O(1)
    curNode = root
    while curNode.leftChild:
        curNode = curNode.leftChild
    return curNode

def deleteNode(root, value): # Time: O(logn) - Space: O(logn)
    if root is None:
        return root
    elif value <= root.data:
        root.leftChild = deleteNode(root.leftChild, value)
    elif value > root.data:
        root.rightChild = deleteNode(root.rightChild, value)
    else:
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp 

        if root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp 

        temp = minValueNode(root.rightChild)
        root.data = temp.data
        root.rightChild = deleteNode(root.rightChild, temp.data)

def deleteBST(root): # Time: O(1) - Space: O(1)
    root.data = None
    root.leftChild = None
    root.rightChild = None    
    return "Success"

rootBST = BSTNode()

insertNode(rootBST, 70)
insertNode(rootBST, 50)
insertNode(rootBST, 90)
insertNode(rootBST, 30)
insertNode(rootBST, 60)
insertNode(rootBST, 80)
insertNode(rootBST, 100)
insertNode(rootBST, 20)
insertNode(rootBST, 40)

deleteBST(rootBST)
inOrderTraversal(rootBST)