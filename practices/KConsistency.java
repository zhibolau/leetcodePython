import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * A team of financial analysts at Amazon has designed a stock indicator to determine the consistency of Amazon's stock in delivering returns daily.
 * More formally, the percentage return (rounded off to the nearest integer) delivered by the stock each day over the last n days is considered.
 * This is given as an array of integers, stock, prices. The stock's k-consistency score is calculated using the following operations:
 * • In a single operation, omit a particular day's return from the stock prices array to get have one less element, then rejoin the parts of the array. This can be done at most k times.
 * • The maximum number of contiguous days during which the daily return was the same is defined as the k-consistency score for Amazon's stock.
 * Note that the return may be positive or negative.As part of the team, you have been assigned to determine the k-consistency score for the stock.
 * You are given an array stock prices of size n representing the daily percentage return delivered by Amazon stock and a parameter k.
 * Determine the k-consistency score.
 * Example:
 * Consider the percentage return delivered by
 * Amazon's Stock in the last 8 days is represented as
 * stock_prices = [1, -2, 1, 1, 3, 2, 1, -2] and K = 3. return The maximum number of contiguous days => 4
 *
 * 给一个数组price，删掉最多K个元素, 求最长的、元素相同的sub array的长度
 * k: maximum number of days that can be removed
 *
 * 创建hashmap，保存元素和对应出现的index，遍历每个元素并做sliding window，时空均为O(n)
 */

public class KConsistency {

    public static void main(String[] args) {
        KConsistency test = new KConsistency();
        int[] test1 = {1, -2, 1, 1, 3, 2, 1, -2}, test2 = {7, 5, 7, 7, 1, 1, 7, 7};

        System.out.println(test.getKConsistency(test1, 2));
        System.out.println(test.getKConsistency(test2, 2));
    }

    public int getKConsistency(int[] stockPrices, int k) {
        Map<Integer, List<Integer>> map = new HashMap<>(); // 元素，对应的index 0 based
        for (int i = 0; i < stockPrices.length; i++) {
            int price = stockPrices[i];
            map.putIfAbsent(price, new ArrayList<>());
            map.get(price).add(i);
        }
        // int[] test1 = {1, -2, 1, 1, 3, 2, 1, -2}
        // {1=[0, 2, 3, 6], -2=[1, 7], 2=[5], 3=[4]}

        int ans = 1; // default to be 1 since each single element can be longest
        for (List<Integer> index : map.values()) {
            int currLen = 0;
            int len = index.size(); // how many times this element appears
            if (len == 1) {
                continue; // same as base case, can be ignored
            }
            int left = 0, right = 1; // 1=[0, 2, 3, 6], price 1 appears on index 0, 2, 3, 6
            // {1, -2, 1, 1, 3, 2, 1, -2} the number of elements need to be deleted between first two 1s: 2-0-1 = 1
            // count between 2 elements: right - left + 1, excluding left and right: right - left + 1 - 2
            int removalCount = index.get(right) - index.get(left) - 1;
            while (right < len) {
                if (left + 1 < right) { // 1=[0, 2, 3, 6], after removing -2, left=0, right=2; after removing 3,2, left=0, right=3
                    // add the new gap generated after incrementing right
                    // left=0, right=2 => gap initially: 1, now += 3-2-1 = 1
                    // left=0, right=3 => gap initially: 1, now += 6-3-1=1+2=3
                    removalCount += index.get(right) - index.get(right - 1) - 1;
                }
                while (removalCount > k) { // too many elements, can't be achieved, need increment i and exclude the count between old and new i
                    left++; // 1=[0, 2, 3, 6], new left = 1, {1, -2, 1, 1, 3, 2, 1, -2}, need to remove element -2, count-=1
                    removalCount -= index.get(left) - index.get(left - 1) - 1;
                }
                // {1, -2, 1, 1, 3, 2, 1, -2} right=1, left=0, currLen = longest len so far after removal: remove -2, currLen= {1,1} =2
                currLen = Math.max(currLen, right - left + 1);
                right++;
            }
            ans = Math.max(ans, currLen);
        }
        return ans;
    }
}


