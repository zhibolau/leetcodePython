# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return self.to_bst(nums,0,len(nums)-1)
    
    def to_bst(self,nums,start,end):
        if start >end:
            return None
        mid = (start+end)//2
        node =TreeNode(nums[mid])
        node.left = self.to_bst(nums,start,mid-1)
        node.right = self.to_bst(nums,mid+1,end)
        return node
#有序数组组成BST