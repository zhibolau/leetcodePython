/**
 * prefixSum 记录从开始到现在的总和。
 * 股票stock[]切一刀，切在哪里时左半边Avg和右半边Avg的差值最小，注意数组0-index，返回月份要+1。
 */
public class FindEarliestMonth {
    public static void main(String[] args) {
        FindEarliestMonth test = new FindEarliestMonth();
        System.out.println(test.findEarliestMonth(new int[]{1,3,2,3}));
    }

    public int findEarliestMonth(int[] stock) {
        int len = stock.length;
        long[] prefixSum = new long[len];
        prefixSum[0] = stock[0];
        for (int i = 1; i < len; i++) {
            prefixSum[i] = prefixSum[i - 1] + stock[i];
        }

        long minimumDiff = Integer.MAX_VALUE;
        int monthIdx = 0;
        for (int i = 0; i < len - 1; i++) { //[1,3,2,3] => [1,4,5,8]
            // i=0,left=1/1, right= 最后一个元素（所有sum）-当前元素前的和
            long leftAvg = prefixSum[i] / (long)(i + 1); //i+1 is the count
            long rightAvg = (prefixSum[len - 1] - prefixSum[i]) / (long) (len - 1 - i); // len-1-i is count
            long diff = Math.abs(leftAvg - rightAvg);
            if (diff < minimumDiff) {
                minimumDiff = diff;
                monthIdx = i;
            }
        }
        return monthIdx + 1;
    }

}
