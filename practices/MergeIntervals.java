import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

/**
 * 最少merge几个区间：比如【[1,2].[2,3].[3,5].[4.5]】 output=1因为【4，5】被merge了
 */
public class MergeIntervals {
    public static void main(String[] args) {
        MergeIntervals test = new MergeIntervals();
        System.out.println(test.merge(new int[][]{{3,8}, {2, 3}, {3, 5}, {4, 5}}));
    }
    int merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        int ans = 0;
        List<int[]> mergeList = new ArrayList<>();
        for (int[] interval : intervals) {
            int left = interval[0];
            int right = interval[1];
            if (mergeList.size() == 0 || left >= mergeList.get(mergeList.size() - 1)[1]) {
                mergeList.add(interval);
            } else {
                mergeList.get(mergeList.size() - 1)[1] = Math.max(right, mergeList.get(mergeList.size() - 1)[1]);
                ans++;
            }
        }
        // mergeList.toArray(new int[ans.size()][2]);
        return ans;
    }
}
