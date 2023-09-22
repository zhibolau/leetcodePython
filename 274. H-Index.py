class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations =sorted(citations)
        
        count = 0
        for i in range(len(citations) -1, -1, -1):
            if citations[i] > count: #当前论文的引用次数要比 被引用的论文的数量 要大
                count += 1
        return count