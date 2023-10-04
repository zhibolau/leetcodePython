class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while m>0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m-1+n] = nums2[n-1]
                n -=1
            else:
                nums1[m-1+n] = nums1[m-1]
                m -=1
        
        if m==0 and n > 0:
            nums1[:n] = nums2[:n]


"""
是要把所有元素放入nums1，所以要比较nums1和nums2的最大元素的大小，放入nums1的位置
可能出现m=2，n=3 且nums1的值都比nums2的大，最后的if会处理
"""