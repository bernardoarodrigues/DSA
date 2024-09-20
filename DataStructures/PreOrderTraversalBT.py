# Priority: Root Node -> Left Subtree -> Right Subtree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(node):
    if not node:
        return
    print(node.data)
    preOrderTraversal(node.leftChild)
    preOrderTraversal(node.rightChild)
    
binaryTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
binaryTree.leftChild = leftChild
binaryTree.rightChild = rightChild

preOrderTraversal(binaryTree)