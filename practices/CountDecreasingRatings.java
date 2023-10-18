/**
 * 给一个integer数组arr，判断有多少个subarray是consecutive decreasing，指这些相邻元素，后一个 = 前一个 - 1。
 * 例子：arr = [4, 3, 2, 5, 9, 8]
 * 符合条件的subarray有 [4], [4, 3], [4, 3, 2], [3], [3, 2], [2], [5], [9], [9, 8], [8]，所以答案是10。
 * 解法：先把arr分成consecutive decreasing的subarray，记录每个subarray的长度，长度为n的subarray有 n * (n + 1) / 2种case。
 * 上面的例子，先分成[4, 3, 2], [5], [9, 8]，记录所有的长度[3, 1, 2]，再对每个长度n求n * (n + 1) / 2，最后相加。
 */
public class CountDecreasingRatings {
    public static void main(String[] args) {
        CountDecreasingRatings test = new CountDecreasingRatings();
        System.out.println(test.countRatings(new int[]{4, 5, 2, 1}));
    }
    public int countRatings(int[] array) {
        int left = 0, right = 1, ans = 0; // right需要从1开始，因为对比right和它前一个数的差是否=1
        while (right < array.length) { // [4, 3, 2, 5, 9, 8]
            if (array[right - 1] - array[right] == 1) {
                ans += right - left;
            } else left = right;
            right++;
        }
        ans += array.length; //加上所有单独的元素
        return ans;
    }
}
