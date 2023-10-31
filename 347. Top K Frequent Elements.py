class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
            
        # 按照频率进行排序
        freq_dict_sorted = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        
        # 取前k个元素返回
        ret = list()
        for i in range(k):
            ret.append(freq_dict_sorted[i][0])
        return ret