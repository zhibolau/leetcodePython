import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * 给一个int数组 记录里面每个数字出现的频率，在每遍历到一个数字的时候，在当前时刻，
 * 总有某个数字出现的频率是当前所有数字里出现次数最多的，这个数字在当前坐标是出现最频繁的那个。
 * 最后，记录这些数字里占据最多的坐标数。比如数组{1，2，3，4}
 * <p>
 * for (int i = 0; i < nums.size(); i++)
 * i = 0: 1总共出现了一次 其他都是0次 1在i=0时是出现最多的
 * i = 1：1总共出现了一次，2总共出现了一次，1 和 2 都是目前出现次数最多的
 * i = 2：1，2，3都是目前出现最多次的
 * i = 3： 1，2，3，4都是目前出现最多次的（因为都只出现了1次）
 * <p>
 * 然后数字1在坐标为0，1，2，3的时候都是出现最多次的 它占据的坐标数是4；
 * 同理数字2在坐标为1，2，3的时候是出现最多次的，它占据的坐标数是3；数字3占据了2个坐标，数字4占据了1个坐标。最终返回占据的最多坐标数，是4
 */

public class FindMaximumMaximaCount {
    public static int MaxiumCount(int[] array) {
        HashMap<Integer, Integer> elemtoTime = new HashMap<>();
        HashMap<Integer, Integer> elemtoMaxTime = new HashMap<>();
        int maxTime = -1;
        for (int elem : array) {
            elemtoTime.put(elem, elemtoTime.getOrDefault(elem, 0) + 1);
            maxTime = Math.max(elemtoTime.get(elem), maxTime);
            for (int k : elemtoTime.keySet()) {
                if (elemtoTime.get(k) == maxTime) {
                    elemtoMaxTime.put(k, elemtoMaxTime.getOrDefault(k, 0) + 1);
                }
            }
        }
        System.out.println("111" + elemtoMaxTime);
        int max = Integer.MIN_VALUE;
        for (int k : elemtoTime.keySet()) {
            max = Math.max(elemtoMaxTime.get(k), max);
        }
        return max;
    }

    public static int MaxmCount(int[] arrray) {
        HashMap<Integer, HashSet<Integer>> coutToElem = new HashMap<>();
        HashMap<Integer, Integer> freqCount = new HashMap<>();
        PriorityQueue<Integer> count = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        Map<Integer, Integer> elemToMaxium = new HashMap<>();
        for (int elem : arrray) {
            if (freqCount.containsKey(elem)) {
                coutToElem.get(freqCount.get(elem)).remove(elem);
            }
            freqCount.put(elem, freqCount.getOrDefault(elem, 0) + 1);
            coutToElem.putIfAbsent(freqCount.get(elem), new HashSet<>());
            coutToElem.get(freqCount.get(elem)).add(elem);
            count.offer(freqCount.get(elem));
            HashSet<Integer> largest = coutToElem.get(count.peek());
            for (int integer : largest) {
                elemToMaxium.put(integer, elemToMaxium.getOrDefault(integer, 0) + 1);
            }
        }
        System.out.println("222" + elemToMaxium);
        System.out.println(freqCount);

        int max = Integer.MIN_VALUE;
        for (int k : freqCount.keySet()) {
            max = Math.max(elemToMaxium.get(k), max);
        }

        return max;
    }

    public static void main(String[] args) {
        System.out.println(MaxmCount(new int[]{1, 1, 2, 3, 4, 4, 3, 3, 2, 2, 2, 2}));
        System.out.println(MaxiumCount(new int[]{1, 1, 2, 3, 4, 4, 3, 3, 2, 2, 2, 2}));
    }
}
