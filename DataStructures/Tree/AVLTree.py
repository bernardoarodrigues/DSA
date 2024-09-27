# AVL Tree: self-balancing binary search tree
# The difference between the heights of left and right subtrees for any node cannot be more than one.

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

def getHeight(root): # Time: O(1) - Space: O(1)
    if not root:
        return 0
    return root.height

def rightRotate(disbalancedNode): # Time: O(1) - Space: O(1)
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalancedNode): # Time: O(1) - Space: O(1)
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(root): # Time: O(1) - Space: O(1)
    if not root:
        return 0
    return getHeight(root.leftChild) - getHeight(root.rightChild)

def insert(root, value): # Time: O(logn) - Space: O(logn)
    if not root:
        return AVLNode(value)
    elif value < root.data:
        root.leftChild = insert(root.leftChild, value)
    else:
        root.rightChild = insert(root.rightChild, value)

    root.height = 1 + max(getHeight(root.leftChild), getHeight(root.rightChild))
    balance = getBalance(root)
    
    # left left -> right rotation of root
    if balance > 1 and value < root.leftChild.data:
        return rightRotate(root)
    
    # left right -> left rotation of child and middle, then right rotation of root
    if balance > 1 and value > root.leftChild.data:
        leftRotate(root.leftChild)
        return rightRotate(root)

    # right right -> left rotation of root
    if balance < -1 and value > root.rightChild.data:
        return leftRotate(root)

    # right left -> right rotation of child and middle, then left rotation of root
    if balance < -1 and value < root.rightChild.data:
        rightRotate(root.rightChild)
        return leftRotate(root)
    
    return root

def minValue(root): # Time: O(logn) - Space: O(logn)
    if root is None or root.leftChild is None:
        return root
    return minValue(root.leftChild)

def delete(root, value): # Time: O(logn) - Space: O(logn)
    if not root:
        return root
    elif value < root.data:
        root.leftChild = delete(root.leftChild, value)
    elif value > root.data:
        root.rightChild = delete(root.rightChild, value)
    else:
        if not root.leftChild:
            temp = root.rightChild
            root = None
            return temp
        elif not root.rightChild:
            temp = root.leftChild
            root = None
            return temp
        temp = minValue(root.rightChild)
        root.data = temp.data
        root.rightChild = delete(root.rightChild, temp.data)
    
    root.height = 1 + max(getHeight(root.leftChild), getHeight(root.rightChild))
    balance = getBalance(root)
    
    # left left -> right rotation of root
    if balance > 1 and getBalance(root.leftChild) >= 0:
        return rightRotate(root)
    
    # left right -> left rotation of child and middle, then right rotation of root
    if balance > 1 and getBalance(root.leftChild) < 0:
        root.leftChild = leftRotate(root.leftChild)
        return rightRotate(root)

    # right right -> left rotation of root
    if balance < -1 and getBalance(root.leftChild) <= 0:
        return leftRotate(root)

    # right left -> right rotation of child and middle, then left rotation of root
    if balance < -1 and getBalance(root.rightChild) > 0:
        root.rightChild = rightRotate(root.rightChild)
        return leftRotate(root)

    return root

def deleteTree(root): # Time: O(1) - Space: O(1)
    root.data = root.leftChild = root.rightChild = None
    return "Success"

avlTree = AVLNode(5)
avlTree = insert(avlTree, 10)
avlTree = insert(avlTree, 15)
avlTree = insert(avlTree, 20)
avlTree = delete(avlTree, 15)
levelOrderTraversal(avlTree)
print(deleteTree(avlTree))
levelOrderTraversal(avlTree)