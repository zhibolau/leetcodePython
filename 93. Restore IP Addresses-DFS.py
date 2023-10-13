class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, sub, ips, ip):
            #sub记录当前加 . 后有几个part
            #ips 为结果
            #s是被截取的一段数字
            if sub == 4:  # should be 4 parts
                if s == '':
                    ips.append(ip[1:])  # remove first '.'
                return
            #还未到 4个部分组成ip，用i来分割s，然后加 . ； 
            for i in range(1, 4):  # the three ifs' order cannot be changed!
                if i <= len(s):  # if i > len(s), s[:i] will make false!!!!
                    if int(s[:i]) <= 255: #s是被截取的一段数字
                        dfs(s[i:], sub + 1, ips, ip + '.' + s[:i]) #注意s[i:]  与 s[:i]
                    if s[0] == '0':
                        break  # make sure that res just can be '0.0.0.0' and remove like '00'

        ips = []
        dfs(s, 0, ips, '')
        return ips
        


        #使用dfs求解。可将题目理解成在一个字符串中加入3个挡板，得到四个子字符串的值都小于255.

