class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''
        for i in digits:
            num +=str(i)

    
        res=int(num)+1

        l_res=str(res)
        res_str=[]
        for i in l_res:
            res_str.append(int(i))
        return res_str
