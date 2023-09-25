#开一个arr数组，遍历magazine的内容记录每个字符出现的个数，
#然后继续遍历ransomNote的内容减去相应字符的个数，
#若出现某个字符的个数小于0，则返回False
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for i in magazine:
            arr[ord(i) - ord('a')] += 1 #ord得到字符的unicode值
        for j in ransomNote:
            arr[ord(j) - ord('a')] -= 1
            if arr[ord(j) - ord('a')] < 0:
                return False
        return True