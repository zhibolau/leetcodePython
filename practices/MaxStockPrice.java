import java.util.HashSet;
import java.util.Set;

/**
 * a group of K consecutive month is said to be observable if no 2 month in the group have the same stock price
 * in other words, all the prices in the period are distinct
 * the sum of stock prices of an observable group of months is called the cumulative observable sum.
 * Given the price of stock for n months, find the maximum possible cumulative observable sum among all the groups of months
 * if there's no observable group, return -1;
 *
 * i.e. stockPrice = [1,2,3,4], and k=2
 * 共有（1，2），（2，3），（3，4）三个长度为k的连续区间，并且每个区间没有重复，最大值为7
 *
 * https://www.1point3acres.com/bbs/thread-844884-1-1.html
 */
public class MaxStockPrice {
    public static void main(String[] args) {
        MaxStockPrice test = new MaxStockPrice();
        System.out.println(test.maxSumOfStock(new int[]{1, 2, 7, 7, 4, 3, 6}, 3));
    }
    public long maxSumOfStock(int[] stockPrice, int k) {
        long ans = 0;
        int left = 0, right = 0;
        Set<Integer> set = new HashSet<>(); //去除duplicate stock price
        while (right < stockPrice.length) { // 使用sliding window，当右指针<len时，如果set已经有了，或者窗口大小 > k
            while (set.contains(stockPrice[right]) || right - left + 1 > k) {
                set.remove(stockPrice[left++]);
            }
            set.add(stockPrice[right]);
            if (right - left + 1 == k) {
                long temp = 0;
                for (Integer price : set) {
                    temp += price;
                }
                ans = Math.max(ans, temp);
            }
            right++;
        }
        return ans == 0 ? -1 : ans;
    }
}
