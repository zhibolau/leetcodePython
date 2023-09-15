class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        cache = {}

        def diff(s):
            if s in cache: return cache[s]
            res = []
            if '+' not in s and '-' not in s and '*' not in s:
                res.append(int(s))
                cache[s] = res
                return res
            for i in range(len(s)):
                if s[i] in '+-*':
                    left = diff(s[:i])
                    right = diff(s[i+1:])
                    for l in left:
                        for r in right:
                            if s[i] == '+': res.append(l+r)
                            elif s[i] =='-': res.append(l-r)
                            else:
                                res.append(l*r)
            cache[s] = res
            return res
        return diff(expression)