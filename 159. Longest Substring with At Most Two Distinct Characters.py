def lengthOfLongestSubstringTwoDistinct(self, s):
    if not s:
        return 0
    n = len(s)
    counter = {}
    longest, left = 0, 0
    for right in range(n):
        counter[s[right]] = counter.get(s[right], 0) + 1
        while right < n and len(counter) > 2: #只可以有两个不同的字母 多了就开减，反正下面longest已经记录max了
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                del counter[s[left]]
            left += 1
        longest = max(longest, right - left + 1)
        
    return longest

#令狐老师的双指针解法和hash map配合使用. 每次循环时判断counter的长度是否超过2，如果超过, 
# 则移动left指针，同时counter中的s【left】减一. 直到counter长度为2，left指针停止移动，直到right指针移动到尾端.