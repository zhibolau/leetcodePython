class TwoSum:
    def __init__(self):
        self.arr = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.arr.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        d = set()
        for val in self.arr:
            if val not in d:
                d.add(value - val)
            else:
                return True
        return False