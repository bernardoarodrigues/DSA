# Priority: Left Subtree -> Right Subtree -> Root Node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def postOrderTraversal(node):
    if not node:
        return
    postOrderTraversal(node.leftChild)
    postOrderTraversal(node.rightChild)
    print(node.data)
    
binaryTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
binaryTree.leftChild = leftChild
binaryTree.rightChild = rightChild

postOrderTraversal(binaryTree)