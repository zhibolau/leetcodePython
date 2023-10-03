class Solution(object):  
    def maxSubarraySumCircular(self, A):

        #### case 1: max appear in the middle
        max_here, max_so_far = -float('inf'), -float('inf')
        for a in A:
            max_here = max(max_here + a,  a)
            max_so_far = max(max_so_far, max_here)

        
        #### case 2: max appear at two ends, so in the middle is min 
        min_here, min_so_far = float('inf'), float('inf')
        Ap = A[1:-1]   ### min cannot appear at two ends ;所以掐头去尾了
        for a in Ap:
            min_here = min(min_here + a,  a)
            min_so_far = min(min_so_far, min_here)

        return max(max_so_far, sum(A) - min_so_far)