/**
 * The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.
 * Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
 * <p>
 * The absolute difference of two numbers is the absolute value of their difference.
 * The average of n elements is the sum of the n elements divided (integer division) by n.
 * The average of 0 elements is considered to be 0.
 * <p>
 * Input: nums = [2,5,3,9,5,3]
 * Output: 3
 * Explanation:
 * - The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
 * - The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
 * - The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
 * - The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
 * - The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
 * - The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
 * The average difference of index 3 is the minimum average difference so return 3.
 */
public class MinimumAverageDifference {
    public static void main(String[] args) {
        MinimumAverageDifference test = new MinimumAverageDifference();
        System.out.println(test.minAvgDiff(new int[]{2, 5, 3, 9, 5, 3}));
    }

    // 时间复杂度on，空间o1
    public int minAvgDiff(int[] nums) {
        long rightSum = 0, leftSum = 0;
        int minIndex = 0;
        int len = nums.length;
        int min = Integer.MAX_VALUE;
        for (int num : nums) {
            rightSum += num;
        }
        for (int i = 0; i < len; i++) {
            leftSum += nums[i];
            rightSum -= nums[i]; // subtract the curr val from right sum
            long avgLeft = leftSum / (i + 1);
            long avgRight = i == len - 1 ? 0 : rightSum / (len - i - 1); // if in the last position, avg is 0
            int diff = (int) Math.abs(avgLeft - avgRight);
            if (diff < min) { // if the abs diff is smaller than the lowest possible avg
                // update and save minIndex
                min = diff;
                minIndex = i;
            }
        }
        return minIndex;
    }
}