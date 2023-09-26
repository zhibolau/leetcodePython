class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        q = collections.deque()
        q.append((beginWord,1))
        while q:
            word,length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(beginWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newword = word[:i] + c + word[i+1:]
                    if newword in wordset and newword !=word: #newword不同于当前的word， 而不是endword
                        wordset.remove(newword)
                        q.append((newword,length+1))
        return 0
                
        