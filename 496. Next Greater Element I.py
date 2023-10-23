class Solution:
    
    def nextGreaterElement(self, nums1, nums2):
        
        stack, g_map = [], {}
        for num in nums2:
            
            while stack and stack[-1] < num:
                g_map[stack.pop()] = num 
            
            stack.append(num)
            
        return [-1 if not num in g_map else g_map[num] for num in nums1]