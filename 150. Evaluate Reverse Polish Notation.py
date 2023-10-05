def  evalRPN(tokens):
    stack = []
    for i in tokens:
        if i not in ['+','-','*','/']:
            stack.append(int(i)) #转换int
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if i == '+': stack.append(op1+op2)
            elif i == '-': stack.append(op1-op2)
            elif i == '*': stack.append(op1*op2)
            else:
                stack.append(int(op1*1.0/op2))
    return stack[0]


#没遇到运算符号就放入stack 遇到了就即时运算