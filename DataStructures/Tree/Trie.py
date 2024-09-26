# trie
# applications: auto completion, spelling checker

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        curNode = self.root

        for c in word:
            node = curNode.children.get(c)
            if node == None:
                node = TrieNode()
                curNode.children.update({c:node})
            curNode = node
        curNode.endOfString = True
        print("Success")

    def searchString(self, word):
        curNode = self.root
        for i in word:
            node = curNode.children.get(i)
            if not node:
                return False
            else:
                curNode = node
        if curNode.endOfString:
            return True
        else:
            return False
        
    def deleteString(self, root, word, index):
            ch = word[index]
            curNode = root.children.get(ch)
            canBeDeleted = False

            if len(curNode.children) > 1:
                self.deleteString(root, word, index+1)
                return False
            if index == len(word)-1:
                if len(curNode.children) >= 1:
                    curNode.endOfString = False
                    return False
                else:
                    root.children.pop(ch)
                    return True
            if curNode.endOfString:
                self.deleteString(curNode, word, index+1)
            canBeDeleted = self.deleteString(curNode, word, index+1)
            if canBeDeleted:
                root.children.pop(ch)
                return True
            else:
                return False

newTrie = Trie()
newTrie.insertString("ABC")
newTrie.insertString("DEF")

print(newTrie.searchString("ABC"))
print(newTrie.searchString("CBA"))

print(newTrie.deleteString(newTrie.root, "ABC", 0))
print(newTrie.searchString("ABC"))