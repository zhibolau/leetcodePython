import java.util.*;

/**
 * Bring exactly one volume of the book in stock for each of the next n days.
 * on the Nth day, all volumes will be in stock. each day you will purchase the maximum number of volumes you can such that:
 * - you have not purchased the volume before;
 * - you already own all prequels (prior volumes)
 * determine the volumes you would purchase each day. You should return an array of n arrays where the ith array contains:
 * - the volume numbers are sorted in increasing order if you purchased some volumes on the ith day
 * - the single element -1 if you did not purchase any book
 *
 * i.e. volume = [2,1,4,3]
 * 一开始所有都是unavailable，第一天可以买2，但是它的prerequisite1你没有，所以不能买 【-1，0，0，0】
 * 第二天出了1，可以买1和2【【-1】，【1，2】，0，0】
 * 第三天出了4，但是不能买【【-1】，【1，2】，【-1】，0】
 * 第四天可以买3，4【【-1】，【1，2】，【-1】，【3，4】】
 *
 * 解法：把书放进min heap里，如果heap top的元素是当前需要的书，就Pop出来。
 *
 * 比如3,2,1,4,5 先把3放进去，然后再把2放进去，再把1放进去。这个时候1在堆顶，而我们需要1这本书，所以Pop出来。
 * 然后我们又需要2这本书了，堆顶恰好是2，所以再pop出来。
 */
public class BookRetail {
    public static void main(String[] args) {
        BookRetail test = new BookRetail();
        int[] vols = new int[] {3,5,1,2,4};
        int[][] ans = test.purchaseBooks(vols);
        for (int[] eachDay : ans) {
            System.out.println(Arrays.toString(eachDay));
        }
    }
    public int[][] purchaseBooks(int[] volumes) {
        int len = volumes.length;
        int[][] ans = new int[len][];
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        int needToBuy = 1; // first day needToBuy = 1 (i+1)
        for (int i = 0; i < len; i++) {
            minHeap.offer(volumes[i]);
            List<Integer> temp = new ArrayList<>();
            // while heap不空，且当前堆顶的数字<need to buy,且temp当前最后一个比堆顶数小1
            while (!minHeap.isEmpty() && minHeap.peek() <= needToBuy && (temp.size() == 0 || temp.get(temp.size() - 1) == minHeap.peek() - 1)) {
                temp.add(minHeap.poll());
                needToBuy += 1;
            }
            // 如果temp有东西，就放入ans，否则是-1
            ans[i] = temp.size() == 0 ? new int[] {-1} : temp.stream().mapToInt(Integer::intValue).toArray();
        }
        return ans;
    }
}
