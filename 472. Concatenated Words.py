class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        res = []
        for w in words:
            if not w:
                continue
            word_set.remove(w)
            if self.dfs(w,word_set,0):
                res.append(w)
            word_set.add(w)
        return res
    
    def dfs(self,word,dict,index):
        if index == len(word):
            return True
        for j in range(index+1,len(word)+1):
            if word[index:j] in dict and self.dfs(word,dict,j):#当前词有单词在dict中 也就是有被别人组成
                return True
        return False
        