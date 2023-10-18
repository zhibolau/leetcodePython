import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * Amazon Shopping has n items in inventory. Each item has a rating that may be negative.
 * The team wants to work on an algorithm that will suggest combinations of these items that customers might buy, or, combos for short.
 * a combo is defined as a subset of given n items. the total popularity of a combo is the sum of the popularises of the individual items in the combo.
 * design an algorithm that can find the k combos with the highest popularity.
 * return an array of k integers where the ith denotes the popularity of ith the best combo, arranged best to worst.
 * You can have empty subset as combos.
 *
 * 先把所有正数相加得到最大值,不会再超过这个数。然后把所有负数变正，并从小到大排序。
 * 接下来就是:减去正数,或者加上负数 => 如果我们把负数都变成正数，那就统一变成了减去正数。
 * 创建一个maxHeap，放int[]，第一位是subArraySum，第二位是当前sub array的最后一个元素index
 * sub array move到下一个元素时要考虑两种情况：包含当前元素和不包含当前元素。
 *
 * i.e. n=3 popularity=[3,5,-2], k=3
 * all possible popularity of combos: 0,3,5,-2,8,3,1,6 => the best 3 are: [8,6,5]
 */
public class KMostPopularCombos {

    public static void main(String[] args) {
        KMostPopularCombos KMostPopularCombos = new KMostPopularCombos();
        int[] popularity = {3,5,-2,7}; //0,3,5,-2,7,8,1,10,3,12,5,13,15 => the best 3 are: [15, 13, 12]
        int[] bestCombos = KMostPopularCombos.bestCombo(popularity, 3);
        System.out.println(Arrays.toString(bestCombos));
    }

    public int[] bestCombo(int[] popularity, int k) {
        int maxSum = 0;
        for (int p : popularity) if (p > 0) maxSum += p; // adding up all positive num
        int[] abs = Arrays.stream(popularity).map(Math::abs).toArray(); // making the negative positive, and sort
        Arrays.sort(abs);

        int len = popularity.length;
        List<Integer> ans = new ArrayList<>();
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        maxHeap.offer(new int[] {maxSum - abs[0], 0}); // maxSum: 15, abs: {2,3,5,7} first put {13, 0}
        ans.add(maxSum);

        while (!maxHeap.isEmpty() && ans.size() < k) { // need to find k elem
            int[] curr = maxHeap.poll();
            int currSum = curr[0]; // {13, 0}
            int index = curr[1];
            ans.add(currSum);
            if (index + 1 < len) {
                maxHeap.offer(new int[] {currSum - abs[index + 1], index + 1}); // next sub array without curr element => curr index=0: 13-3, 1
                maxHeap.offer(new int[] {currSum - abs[index + 1] + abs[index], index + 1}); // next sub array with curr element => 13-3+2, 1
            }
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}