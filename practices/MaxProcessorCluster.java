import java.util.PriorityQueue;

/**
 * 一排机器，input第一个是一个数组，代表每个机器的processing power，第二个数组代表boosting power, 第三个整数Max power。
 * 要求出满足条件最长的cluster（连续的sub array），满足: max(boosting power) + sum(processing power) * k  < maxPower，k是这个subarray的长度。
 * Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.
 * https://leetcode.com/problems/maximum-number-of-robots-within-budget/
 * 解法：keep track of the max using maxHeap, until it exceeds the maxPower => start removing from the start using pointer j
 */
public class MaxProcessorCluster {
    public static void main(String[] args) {
        MaxProcessorCluster test = new MaxProcessorCluster();
        System.out.println(test.maximumRobots(new int[]{3, 6, 1, 3, 4}, new int[]{2, 1, 3, 4, 5}, 25));
    }
    //时间复杂度O(nlogn)
    public int maximumRobots(int[] processingPower, int[] bootingPower, long powerMax) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        int len = bootingPower.length;
        int ans = Integer.MIN_VALUE;
        long cost = 0;
        for (int i = 0, j = 0; i < len; i++) {
            cost += bootingPower[i];
            maxHeap.add(processingPower[i]);
            while (!maxHeap.isEmpty() && (maxHeap.peek() + maxHeap.size() * cost > powerMax)) {
                maxHeap.remove(processingPower[j]);
                cost -= bootingPower[j];
                j++;
            }
            ans = Math.max(ans, maxHeap.size());
        }
        return ans;
    }
}
