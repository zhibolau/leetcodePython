class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"  #num是进位
        for i in xrange(len(s)):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1: #这里不能用elif
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)
    


    #若全部用if语句，程序运行时会遍历所有if（不管每个if后的逻辑运算是否为True）。
    # 而用if-elif，程序运行时，只要if或后续某一个elif之一满足逻辑值为True，
    # 则程序执行完对应输出语句后自动结束该轮if-elif（即不会再去冗余地执行后续的elif或else）。
    # 程序执行效率更高，在项目越庞大代码越多的情况下体现越明显。
