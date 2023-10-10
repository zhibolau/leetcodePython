class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        n = len(A)
        m = len(A[0])
        k = len(B[0])

        C = [[0] * k for i in range(n)]

        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    for l in range(k):
                        C[i][l] += A[i][j] * B[j][l]
        return C
    

    #一种时间复杂度也为 
O
(
k
∗
n
2
)
 的办法（k 为一行中的非零位个数） 这种办法比较巧妙，通过初始化结果矩阵，然后把非零位逐个累乘累加的办法，而不是按照原来的矩阵乘法顺序在做。