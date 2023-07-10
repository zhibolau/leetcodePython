class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        matches = self.map[key]

        result = ''

        left = 0
        right = len(matches) -1
        while left <= right:
            mid = (right + left) // 2
            if matches[mid][1] <= timestamp:
                left= mid + 1
                result = matches[mid][0]
            else:
                right = mid - 1
        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)