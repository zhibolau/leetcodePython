/**
 * 给一组数组, 删掉k个连续元素, 问剩下最小的和是多少?
 * 解法：sliding window, 求长度为K的subarray的和的最大值，然后用总和减去
 */
public class MinSum {
    public static void main(String[] args) {
        MinSum test = new MinSum();
        System.out.println(test.getMinSum(new int[]{2, 15, -3, 4, 6, 1, 5}, 4));
    }
    public int getMinSum(int[] nums, int k) {
        int left = 0, right = 0, maxSum = 0, currSum = 0, totalSum = 0;
        while (right < nums.length) {
            currSum += nums[right];
            totalSum += nums[right];
            if (right - left + 1 >= k) {
                maxSum = Math.max(currSum, maxSum);
                currSum -= nums[left++];
            }
            right++;
        }
        return totalSum - maxSum;
    }
}
