def findSubArrays(nums): #subarray sum is 0
    out =  []
    n = len(nums)
    i = 0
    while (i < n) :
        prefix = 0
        j = i
        while (j < n) :
            prefix += nums[j]
            if (prefix == 0) :
                out.append([i, j])
            j += 1
        i += 1
    return out
# i从头开始  i固定 j一直往后走 只要小于 len，就sum


print(findSubArrays([6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]))
#[[0, 10], [2, 4], [2, 6], [5, 6], [6, 9]]