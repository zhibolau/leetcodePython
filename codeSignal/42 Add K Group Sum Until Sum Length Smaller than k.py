# // 042 Add K Group Sum Until Sum Length Smaller Than K

# // Python version of code, it can be easily changed into java

def addKGroupSumUntilSumLengthSmallerThanK(inputstr, k):

    curstr = inputstr
    while len(curstr) > k:
        group = len(curstr) // k 
        if len(curstr) % k != 0:
            group += 1
        itrvals = ['']*group #//char[] itrvals = new char[group];
        for g in range(group):
            subsum = 0
            for i in range(k):
                if i +g*k == len(curstr):
                    break
                subsum += int(curstr[i+g*k])
            itrvals[g] = str(subsum)
        curstr = ''.join(itrvals) #//curstr = String.valueof(itrvals)
    return curstr
