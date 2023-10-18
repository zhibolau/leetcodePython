import java.util.HashMap;
import java.util.Map;

/**
 * deliver boxes as few trips as possible: choose either rules =>
 * 1. choose 2 packages with the same weight
 * or 2.choose 3 packages with the same weight
 * determine the minimum number of trips required to deliver the packages
 * if not possible to deliver all, return -1
 *
 * i.e. [2,4,6,6,4,2,4] => [4,4,4]-[6,6]-[2,2] -> result: 3 时空复杂度O(n)
 */
public class MoveBoxes {
    public static void main(String[] args) {

    }
    // 构造map存包裹和次数，如果1次肯定不行，其他的使用（double）次数/3，向上取整
    public int minimumRounds(int[] tasks) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for (int task : tasks) {
            map.put(task, map.getOrDefault(task, 0) + 1);
        }
        for (int num : map.values()) {
            if (num == 1) return -1;
            ans += Math.ceil((double) num / 3);
        }
        return ans;
    }
}
