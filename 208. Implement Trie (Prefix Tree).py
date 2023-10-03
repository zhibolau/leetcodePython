class TrieNode:
    def __init__(self):
        self.child = {} #store every inserted word's letter
        self.is_word = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node =self.root
        for letter in word:
            if letter not in node.child:
                node.child[letter]=TrieNode()
            node = node.child[letter]
        node.is_word =True

    def find(self,word): #return found node or None
        node = self.root
        for letter in word:
            node=node.child.get(letter)
            if not node:
                return None
        return node


    def search(self, word: str) -> bool:
        node = self.find(word)
        return self.find(word) is not None and node.is_word


    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)