class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations =sorted(citations)
        
        count = 0
        for i in range(len(citations) -1, -1, -1):
            if citations[i] > count: #引用次数要比第几个论文要大
                count += 1
        return count