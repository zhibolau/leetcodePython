class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i]=d.get(i,0) +1

        sort_nums=sorted(d.items(), key=lambda x: x[1],reverse=True)

        res = []
        for k,v in sort_nums:
            res.append(k*v)

        return ''.join(res)
    

#same as 347