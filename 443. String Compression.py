class Solution:
    def compress(self, chars) -> int:
        if len(chars) == 1:
            return 1
        new = []
        curr, next = 0, 1
        
        while next < len(chars):  
            count = 1
            while next < len(chars) and chars[next] == chars[curr]:
                count += 1
                next += 1
                
            if count == 1: 
                new.append(chars[curr]) # ['a']
            else:
                new.append(chars[curr])
                new.extend(list(str(count)))  # str(12) list(str(count)) = ['1','2']  extend would add '1','2' to list
                
            curr = next
            next += 1
            
        if curr == len(chars)-1: #处理末尾有个与前一个位置不同的字母
            new.append(chars[curr])
            
        chars[:] = new #题目要求把原输入修改了
        return len(new)
