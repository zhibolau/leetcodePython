# for i, ch in enumerate('ssadfasdfasdf'):
# 	print i,ch
	


def print_zip():
    print('tuple format ----->')
    for (a, b), c in zip(equations, values):#[["a","b"],["b","c"]], values = [2.0,3.0]
        print((a, b), c)
    print('----------------------')
    print('no format ----->')
    for i in zip(equations, values):#[["a","b"],["b","c"]], values = [2.0,3.0]
        print(i)


def is_palindrome(s):
    print('----------------------')
    print(s)
    return s == s[::-1]
    # [::-1] means reverse the string: start at the end of the string and end at position 0, 
    # move with the step -1 ,  negative one, which means one step backwards

def and_oper(a,b):
    # a, b both true, return last true element
    return a and b

    # & is bit operation 0100 & 0101 =0100 = 4


if __name__ == '__main__':


    a = [1,2,3,4]
    print(a[:-1])
    print(a[1:-1])
    print(a[-1])
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    #print_zip()

    str1 = 'aa'
    
    str2 ='ab'
    str3 ='a'
    # print(is_palindrome(str1))
    # print(is_palindrome(str2))
    # print(is_palindrome(str3))

    a = 1
    b = 2
    c = 0
    print(and_oper(a , b))
    print(and_oper(a , c))