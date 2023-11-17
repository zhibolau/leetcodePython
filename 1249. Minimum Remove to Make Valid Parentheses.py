class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        state_dict={}
        for idx, character in enumerate(s):
            if character=="(":
                stack.append(idx)
            if character==")" and len(stack)>0 :
                state_dict[idx]=True
                state_dict[stack[-1]]=True
                stack.pop()
                
        res=[]
        for idx, ch in enumerate(s):
            if ch=="(" or ch== ")":
                if idx in state_dict:
                    res.append(ch)
            else:
                res.append(ch)
        
        return res
        