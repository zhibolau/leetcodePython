import java.util.Arrays;

/**
 * Taking the change in temperature data of n days, the aggregate temperature change evaluated on the ith day
 * is the maximum of the sum of the changes in the temperature until the ith day, and the sum of the change in
 * temp in the next (n-i) days, with the ith day temp change included in both
 *
 * Given the temp data of n days, find the max aggregate temp change evaluated among all the days
 * i.e.[6, -2, 5] => maximum change (9, 4, 9) = 9
 * day1: change before: 6, change after:6-2+5 = 9
 * day2: change before: 6-2 =4, change after: -2+5 = 3
 * day3: change before: 6-2+5 = 9, change after: 5
 */
public class MaxAggregateTemperatureChange {
    public static void main(String[] args) {
        MaxAggregateTemperatureChange test = new MaxAggregateTemperatureChange();
        System.out.println(test.maxTempChange(new int[]{2,5,-4,-3,1}));
    }
    public long maxTempChange(int[] temps) {
        int len = temps.length; // [2,5,-4,-3,1]
        long[] prefixSum = new long[len]; // [2,7,3,0,1]
        prefixSum[0] = temps[0];
        for (int i = 1; i < len; i++) {
            prefixSum[i] = prefixSum[i - 1] + temps[i];
        }
        //初始值，第一天或最后一天的和大
        long max = Math.max(prefixSum[0], prefixSum[len - 1]); //max(2,1)

        for (int i = 1; i < len; i++) {
            // i=1, max(7,1-2), i=2, max(3,1-7)...
            // 遍历preSum数组，当前数字所指即为之前的和，最后一位元素-当前元素前一位：从当前到最后的和，取2者max
            long temp = Math.max(prefixSum[i], prefixSum[len - 1] - prefixSum[i - 1]);
            max = Math.max(max, temp);
        }
        return max;
    }
}
