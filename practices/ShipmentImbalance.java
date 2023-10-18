import java.util.Stack;

/**
 * 求array的所有subArray的 max - min的和总和.
 * You are given an integer array nums.
 * The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
 * Return the sum of all subarray ranges of nums.
 * A subarray is a contiguous non-empty sequence of elements within an array.
 * <p>
 * https://leetcode.com/problems/sum-of-subarray-ranges/ 2104
 * <p>
 * i.e. [1,2,3] subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3] => 注意，【1，3】不连续，不行
 * range   ： 0，   0，  0，   1，     1,     3-1=2 => return 1+1+2=4
 * <p>
 * https://leetcode.cn/problems/sum-of-subarray-minimums/solution/xiao-bai-lang-dong-hua-xiang-jie-bao-zhe-489q/
 * 相似题解：找到自数组的最小值之和：A=【3，1，2，4，1】，先求出最小值的辐射范围，比如一段数字中包含1， 则这段数字的最小值肯定为1
 * 【3，1，2，4，1】【3，1，2，4】【3，1，2】【3，1】的最小值都为1，=》元素1的辐射范围
 * 所以数组A，index0的元素3的辐射范围【3】，index1的元素1的辐射范围【3，1，2，4，1】。。。
 * 每个元素E的辐射范围都是一个连续数组，因此E在每个子数组的贡献值都为E，如果子数组有n个，总贡献值为n*E
 * 假设辐射左边界为left，右边界为right，元素index i，则左边届在【left，i】选取，右边界在【i， right】选取
 * 子数组个数为：(i-left+1) * (right-i+1)，元素A【i】的总贡献值为A[i]*(i-left+1)*(right-i+1)
 * 步骤：
 * 利用单调栈向左找到第一个比A[i]小的数A[left]（遍历顺序为0->n-1)，也就是E辐射范围的左边界；
 * 利用单调栈向右找到第一个比A[i]小的数A[right]（遍历顺序为n-1->0)，也就是E辐射范围的右边界；
 * 将每个元素的贡献值求和得到最终答案
 * <p>
 * 假定我们能预处理出两数组 l 和 r 分别代表 arr[i]arr[i] 作为子数组最小值时，其所能到达的最远两端：
 * <p>
 * l[i] = a 代表下标 a 为 arr[i] 能够作为子数组最小值时的最远左边界，即为 arr[i] 左边第一个比其小的元素（若不存在，则为 a = -1）
 * r[i] = b 代表跳表 b 为 arr[i] 能够作为子数组最小值时的最远右边界，即为 arr[i] 右边第一个比其小的元素（若不存在，则为 b = n）
 * 子数组左端点个数为 (i - a) 个，右端点个数为 (b - i) 个，根据乘法原理可知，子数组个数为两者乘积，每个子数组对答案的贡献为 arr[i]。
 * <p>
 * 由于 arr 可能有重复元素，我们需要考虑取左右端点时，是取成「小于等于」还是「严格小于」：
 * <p>
 * 若两端均取成严格小于，且两端中间存在与 arr[i] 等值元素，会导致相同子数组被重复统计；
 * 若两端均取成小于等于，且两端恰好存在与 arr[i] 等值元素，会导致原本可以被添加到子数组的等值元素漏加；
 * 若一端取成严格小于，另一端取成小于等于，可确保不重不漏。
 * 至于预处理 l 和 r 则可以使用「单调栈」求解。
 * <p>
 * 次题和上面非常相似，除了找到min值以外，还需要找到max值，所以用两个stack记录
 * https://leetcode.com/problems/sum-of-subarray-ranges/discuss/2413551/2-Monotonic-stack-easy-to-understand-plus-a-lot-of-explanations
 */
public class ShipmentImbalance {
    public static void main(String[] args) {
        ShipmentImbalance test = new ShipmentImbalance();
        System.out.println(test.subArrayRanges(new int[] {1,2,3}));
    }

    // O(n)
    public long subArrayRanges(int[] nums) {
        return sumSubarrayMaxs(nums) - sumSubarrayMins(nums);
    }

    public long sumSubarrayMins(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        int n = nums.length;
        long count = 0;
        // stack save the index of the elem that's smaller than curr element
        for (int i = 0; i <= n; i++) { //[1,3,2] first push 0, nums[0]=1 < nums[1]=2, 不进入while，push 1

            while (!stack.isEmpty() && (i == n || nums[stack.peek()] > nums[i])) {
                int mid = stack.pop();
                int left = mid - (stack.isEmpty() ? -1 : stack.peek());
                int right = i - mid;
                count += (long) nums[mid] * (left) * (right);
            }
            stack.push(i);
        }
        return count;
    }

    public long sumSubarrayMaxs(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        int n = nums.length;
        long count = 0;

        for (int i = 0; i <= n; i++) {
            while (!stack.isEmpty() && (i == n || nums[stack.peek()] < nums[i])) {
                int mid = stack.pop();
                int left = mid - (stack.isEmpty() ? -1 : stack.peek());
                int right = i - mid;
                count += (long) nums[mid] * (left) * (right);
            }
            stack.push(i);
        }
        return count;
    }

    // O(n^2)
    public static long shipmentImbalance(int[] weights) {
        int n = weights.length;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int min = weights[i], max = weights[i];
            for (int j = i + 1; j < n; j++) {
                min = Math.min(min, weights[j]);
                max = Math.max(max, weights[j]);
                ans += max - min;
            }
        }
        return ans;
    }
}
