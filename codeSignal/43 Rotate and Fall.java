// 043 Rotate and Fall
// similar to leetcode move zeros.
// move zeros: given an integer array contains 0s, move all 0s to the right part of this array, while moving, maintain the relative order of other non zero elements.


class Solution {
    public void moveZeroes(int[] nums) {
        if(nums == null || nums.length == 0) return;
        int m = nums.length;
        int i = 0;
        int j = 0;
        while (i < m) {
            if (nums[i] != 0) {
                nums[j++] = nums[i];
            }
            i++;
        }
        while (j < m) {
            nums[j++] = 0;
        }
        
    }
}
