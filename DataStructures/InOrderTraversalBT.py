# Priority: Left Subtree -> Root Node -> Right Subtree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def inOrderTraversal(node): # Time: O(n) - Space: O(n)
    if not node:
        return
    inOrderTraversal(node.leftChild)
    print(node.data)
    inOrderTraversal(node.rightChild)
    
binaryTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
binaryTree.leftChild = leftChild
binaryTree.rightChild = rightChild

inOrderTraversal(binaryTree)