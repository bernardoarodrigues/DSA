# binary tree (with linked list)

# Traverses from first to last level, from left to right
# Level: distance from root + 1

import QueueWithLinkedList

class TreeNode:
    def __init__(self, data): # Time: O(1) - Space: O(1)
        self.data = data
        self.leftChild = None
        self.rightChild = None

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

def search(node, value): # Time: O(n) - Space: O(n)
    if not node:
        return
    customQueue = QueueWithLinkedList.Queue()
    customQueue.enqueue(node)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if(root.value.data == value):
            return "Node found"
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)
    return "Node not found"

def insertNode(root, newNode): # Time: O(n) - Space: O(n)
    if not root:
        root = newNode
    else:
        customQueue = QueueWithLinkedList.Queue()
        customQueue.enqueue(root)
        while not(customQueue.isEmpty()):
            node = customQueue.dequeue()
            if node.value.leftChild:
                customQueue.enqueue(node.value.leftChild)
            else:
                node.value.leftChild = newNode
                return "Inserted"
            
            if node.value.rightChild:
                customQueue.enqueue(node.value.rightChild)
            else:
                node.value.rightChild = newNode
                return "Inserted"
            
def getDeepestNode(root):
    deepestNode = None
    if not root:
        return
    customQueue = QueueWithLinkedList.Queue()
    customQueue.enqueue(root)
    while not(customQueue.isEmpty()):
        node = customQueue.dequeue()
        deepestNode = node.value
        if node.value.leftChild:
            customQueue.enqueue(node.value.leftChild)
        if node.value.rightChild:
            customQueue.enqueue(node.value.rightChild)
    return deepestNode

def deleteDeepestNode(root, deepestNode):
    if not root:
        return
    customQueue = QueueWithLinkedList.Queue()
    customQueue.enqueue(root)
    while not(customQueue.isEmpty()):
        node = customQueue.dequeue()
        if node.value is deepestNode:
            node.value = None
            return
        if node.value.rightChild:
            if node.value.rightChild is deepestNode:
                node.value.rightChild = None
                return
            else:
                customQueue.enqueue(node.value.rightChild)
        if node.value.leftChild:
            if node.value.leftChild is deepestNode:
                node.value.leftChild = None
                return
            else:
                customQueue.enqueue(node.value.leftChild)
    
def deleteNode(root, node): # Time: O(n) - Space: O(n)
    if not root:
        return
    customQueue = QueueWithLinkedList.Queue()
    customQueue.enqueue(root)
    while not(customQueue.isEmpty()):
        curNode = customQueue.dequeue()
        if curNode.value.data is node:
            deepestNode = getDeepestNode(root)
            curNode.value.data = deepestNode.data
            deleteDeepestNode(root, deepestNode)
            return "Success"
        if curNode.value.leftChild:
            customQueue.enqueue(curNode.value.leftChild)
        if curNode.value.rightChild:
            customQueue.enqueue(curNode.value.rightChild)

def deleteTree(root):
    root.data = None
    root.leftChild = None
    root.rightChild = None

rootBinaryTree = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftChild = tea
hot.rightChild = coffee
rootBinaryTree.leftChild = hot
rootBinaryTree.rightChild = cold

deleteTree(rootBinaryTree)
levelOrderTraversal(rootBinaryTree)