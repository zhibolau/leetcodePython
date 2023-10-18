import java.util.Arrays;
import java.util.PriorityQueue;

/**
 * given an array representing the location of N vegetarian restaurants in the city, implement an algorithm to find the nearest X restaurants to the customer's location
 * input:
 * 1. all locations, a list of elements consists of a pair of integers represent x and y coordinates
 * 2. number of restaurants, and integer representing the number of nearby restaurants to be returned
 * output:
 * return a list of elements of x,y, if there's a tie, use location with the closest x coordinate
 * if no location is possible, return a list with an empty location, not just empty list
 *
 * lc 973
 * The distance between two points on the X-Y plane is the square root of x^2 + y^2
 */

public class KClosestPointsToOrigin {

    public static void main(String[] args) {
        KClosestPointsToOrigin kClosestPointsToOrigin = new KClosestPointsToOrigin();
        int[][] op = kClosestPointsToOrigin.kClosest(new int[][]{{0, 1}, {1, 0}}, 2);
        for (int[] x : op) {
            System.out.println(x[0] + " " + x[1]);
        }
    }

    public int[][] kClosest(int[][] points, int k) {

        // closest k elements are required, create a maxHeap of size k, longer distance will be stored on top
        // the lowest k distance elements will remain in the heap

        // pq by default is minHeap, rewrite Comparator to have maxHeap base on distance
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] * b[0] + b[1] * b[1] - (a[0] * a[0] + a[1] * a[1]));

        for (int[] point : points) {
            maxHeap.offer(point);
            if (maxHeap.size() > k) {
                maxHeap.poll(); // keep polling out the element if size > k
            }
        }
        int[][] ans = new int[k][2];

        while (k-- > 0) { // fill in the answer array
            ans[k] = maxHeap.poll();
        }
        return ans;
        // 时间复杂度O(NlogN), N is the length of points. 空间O(n).
    }

    /**
     * 还可以使用快排，达到时空均为O(n)
     * 先定义getDistance方法，和swap方法，定义partition方法，把最左元素作为anchor，从下一个开始遍历至right inclusive
     * 如果distance比pivot小，则需要放在j的左边，如果大则不需要动，因为已经在j的右边了。跳出循环后，把anchor pivot元素放到指定位置
     * 定义quickSort方法(points，left, right, k)，当left<right，找到pivot的index，并计算出左边元素的长度，分别递归k and k-leftLen。
     */
    public int[][] kClosestQuickSort(int[][] points, int k) {
        quickSort(points, 0, points.length - 1, k);
        return Arrays.copyOfRange(points, 0, k);
    }

    private void quickSort(int[][] points, int left, int right, int k) {
        if (left < right) {
            int index = partition(points, left, right); // find the position of pivot, then do left/right of pivot
            int leftLen = index - left + 1;
            quickSort(points, left, index - 1, k);
            quickSort(points, index + 1, right, k - leftLen);
        }
    }

    private int partition(int[][] points, int left, int right) {
        int mid = (left + right) / 2;
        swap(points, mid, left); // randomize mid, and put it all the way to the left
        int pivot = dist(points, left); // get the distance
        int j = left;
        for (int i = j + 1; i <= right; i++) { // elem on left is anchor, iterate through the next element of it, till right (inclusive)
            if (dist(points, i) < pivot) { // if the distance smaller than pivot, put to left of j (increment j, and swap i, j)
                j++;
                swap(points, i, j);
            } // don't need to do anything if greater than pivot -> already to the right of j
        }
        swap(points, j, left); // put pivot where it supposed to be (middle)
        return j;
    }

    private void swap(int[][] points, int i, int j) {
        int[] temp = points[i];
        points[i] = points[j];
        points[j] = temp;
    }

    private int dist(int[][] points, int i) {
        return points[i][0] * points[i][0] + points[i][1] * points[i][1];
    }

}
