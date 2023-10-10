# 044 Figure Under Gravity


def figureEnderGravity(matrix):
    if not matrix or not matrix[0]:
        return matrix
    m, n = len(matrix), len(matrix[0])
    minstep = sys.maxsize
    for j in range(n):
        i = 0
        while i < m:
            while i < m and matrix[i][j] != 'F':
                i += 1
            if i == m:
                continue
            while i < m and matrix[i][j] == 'F':
                i += 1
            if i < m:
                cnt = 0
                while i < m and matrix[i][j] != '#':
                    i += 1
                    cnt += 1
                minstep = min(minstep, cnt)
    if minstep == sys.maxsize or minstep == 0:
        return matrix

    for i in range(m-1, minstep-1, -1):
        for j in range(n):
            if matrix[i-minstep][j] == 'F':
                matrix[i][j] = 'F'
                matrix[i-minstep][j] = '.'

    return matrix
