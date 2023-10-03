#https://www.jianshu.com/p/d9972db1571f  dict tree 图示
class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node =self.root
        for letter in word:
            if letter not in node.child:
                node.child[letter]=TrieNode()
            node = node.child[letter]
        node.is_word =True
        

    def search(self, word: str) -> bool:
        def dfs(node,index):
            if index == len(word):
                return node.is_word
            if word[index] =='.':
                for child in node.child.values():
                    if dfs(child,index+1):
                        return True
            if word[index] in node.child:
                return dfs(node.child[word[index]],index+1)
            return False
        return dfs(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)