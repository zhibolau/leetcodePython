import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * The inefficiency of a team is defined as the absolute difference between the skills of the 2 developers.
 * Given the skill values of n developers, find the k teams with the lowest inefficiencies among all possible pairs of teams.
 * Return their inefficiencies sorted ascending.
 * i.e. n=3, skill=[6,9,1], k=2
 * following teams are possible: (6,9)-> diff=3; (6,1)-> diff=5; (9,1)-> diff=8 [3,5,8]
 * the first 2 smallest number is: 3 & 5, return [3,5]
 */
public class SmallestInefficiencies {
    public static void main(String[] args) {
        SmallestInefficiencies test = new SmallestInefficiencies();
        System.out.println(Arrays.toString(test.getSmallestInefficiencies(new int[]{6, 3, 5, 9, 1}, 3)));
    }
    public int[] getSmallestInefficiencies(int[] A, int k) {
        Arrays.sort(A); // [1,6,9]
        // minHeap, int[], 按照第0个元素(diff)从小到大排列, 肯定是挨着的两个元素diff最小
        PriorityQueue<int[]> minheap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        for (int i = 1; i < A.length; i++){
            int diff = A[i] - A[i-1];
            minheap.offer(new int[]{diff, i - 1, i}); //[diff, leftIndex, rightIndex]
        }

        int[] ans = new int[k];
        while(k > 0 && !minheap.isEmpty()){
            int[] curr = minheap.poll();
            int diff = curr[0], left = curr[1], right = curr[2];
            ans[--k]= diff; // 需要先--再赋值，因为此时k是len，越界了，从后往前赋值
            if (right < A.length -1){ // 比如[1,3,5,6,9], left=2, right=3时，diff=6-5=1，此时还要考虑9-5是否也小，放入pq
                int alternativeDiff = A[right + 1] - A[left];
                // 把right向右移动一位，与left做diff，放入pq，比如[1,7,8,9], left=1, right=2, diff=8-7=1, 但是9-7依旧比7-1小
                minheap.offer(new int[]{alternativeDiff, left, right + 1});
            }
        }
        Arrays.sort(ans);
        return ans;
    }
}
