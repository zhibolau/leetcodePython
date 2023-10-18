/**
 * 把 k 个 0 变成 1 后最长的 1, 滑动窗口保持当前window最多只有k个0.
 */
public class MaxConsectiveOnes {
    public static void main(String[] args) {
        MaxConsectiveOnes test = new MaxConsectiveOnes();
        System.out.println(test.longestOne(new int[]{1, 0, 0, 1, 1, 0, 1, 0, 0}, 3));
    }
    public int longestOne(int[] nums, int k) {
        int left = 0, right = 0, ans = 0;
        while (right < nums.length) {
            if (nums[right] == 0) k--;
            while (k < 0) {
                if (nums[left++] == 0) k++;
            }
            ans = Math.max(ans, right - left + 1);
            right++;
        }
        return ans;
    }
}
