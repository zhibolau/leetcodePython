import random
class RandomizedSet(object):

    def __init__(self):
        self.nums = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.nums:
            return False
        self.nums[val] = None
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        return self.nums.pop(val, False) != False
        

    def getRandom(self):
        """
        :rtype: int
        """
        rand = random.randrange(len(self.nums))
        return self.nums.keys()[rand]
        
#法 2 
    def __init__(self):
        self.nums = []
        self.val2index = {}

    def insert(self, val: int) -> bool:
        if val in self.val2index:
            return False
        self.nums.append(val)
        self.val2index[val] = len(self.nums) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.val2index:
            return False
        last = self.nums[-1]
        index = self.val2index[val]

        self.nums[index] = last
        self.val2index[last] = index
        
        del self.val2index[val]
        self.nums.pop()
        return True
        

    def getRandom(self) -> int:
        return self.nums[random.randint(0,len(self.nums)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()