def digitAnagrams(nums):
    if nums is None or len(nums) < 2:
        return 0
    res = 0
    map = {}
    for num in nums:
        temp = list(str(num))
        temp.sort()
        key = ''.join(temp)
        map[key] = map.get(key, 0) + 1
    for v in map.values():
        if v != 1:
            res += v * (v - 1) // 2
    return res


print(digitAnagrams([25, 35, 872, 228, 53, 278, 872]))