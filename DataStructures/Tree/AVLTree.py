# AVL Tree: self-balancing binary search tree
# The difference between heights of left and right subtrees for any node cannot be more than one.

import QueueWithLinkedList

class AVLNode:
    def __init__(self, data=None): # Time: O(1) - Space: O(1)
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

avlTree = AVLNode(10)
