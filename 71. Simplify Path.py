def  simplifyPath(path):
    result = []
    path_list = path.split('/')
    
    for i in path_list:
        if i:
            if i == '..': #回到上一层目录
                if result:
                    result.pop() #所以删除掉当前的目录
            elif i == '.':#当前目录
                continue
            else:
                result.append(i)
    res = '/' + '/'.join(result) # join只会在result的元素中间加/， leading的/还是要单独加出来
    return res