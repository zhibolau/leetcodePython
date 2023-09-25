class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        pattern_map = {}
        for i,j in enumerate(pattern):
            if j not in pattern_map:
                pattern_map[j] = words[i]
            else:
                if pattern_map[j] != words[i]:
                    return False
        num_k = len(pattern_map)
        num_val = len(set(pattern_map.values())) #key value可能出现不同数量，不同key对应一个值 要排除
        return num_k == num_val