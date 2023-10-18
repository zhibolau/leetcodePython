import java.util.Arrays;

/**
 * 给了一个List, 和一个Int k。要你找出满足k - List.size( )个大小的最小缺失数字和。
 * Example: [1, 3, 5, 7, 10] k = 7;
 * Process: miss nums: 2, 4, 6, 8, 9;
 * res: 我们需要 7 - 5 = 2 个缺失数字， 要想和最小，那就从头开始选，那就是2 + 4 = 6，
 * 所以最后return 6
 * https://leetcode.com/problems/append-k-integers-with-minimal-sum/ 原题中k是要添加的数，本题为k-len是要添加的数
 * 因为sort了array，时间复杂度O（nlogn）
 */
public class MinimalKSum {
    public static void main(String[] args) {
        MinimalKSum test = new MinimalKSum();
        System.out.println(test.minimalKSum(new int[]{1, 4, 25, 10, 25}, 7));
    }
    public long minimalKSum(int[] nums, int k) {
        Arrays.sort(nums);
        int prev = -1;
        long sum = 0;
        k -= nums.length; // 新的k为添加的num数量
        for (int num : nums) {
            if (prev == num) continue; // 如果原数组中的dup，跳过
            // If num > k, we already found enough k numbers
            if (num > k) break; // num=5 时，停止
            k++; //更新后k=2，[1, 3, 5, 7, 10]，第一次num=1，k++=3, 第二次num=3, 不大于k，继续, k=4
            sum += num; // sum+=1 = 1, sum+=3 = 4, sum+=5 = 9
            prev = num;
        }

        return (long)(k + 1) * k / 2 - sum; // 相当于求从1-k的总和，再减去数组中原有的数字和
    }
}
