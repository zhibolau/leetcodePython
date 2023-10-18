import java.util.HashMap;
import java.util.Map;

/**
 * There are n processes to be executed, where the ith process takes execution [i] amount of time to execute.
 * Two processes are cohesive if and only if their original execution times are equal.
 * When a process with execution time and simultaneously reduces the execution time of all its cohesive process to ceil(execution[i] / 2).
 *
 * Given the execution time of n processes, find the total amount of time the processor takes to execute all the processes if you execute the processes in the given order, i.e. from left to right.
 *
 * The ceil() function returns the smallest integer that is bigger or equal to its argument. For example, ceil(1.1) = 2, ceil(2.5) = 3, ceil(5) = 5, etc.
 * If the execution time of some process is reduced and becomes equal to the execution time of any other process,
 * then the two processes i and j are not considered cohesive.
 *                        0  1  2  3  4  5 => index
 * i.e: n=6, execution = [5, 5, 3, 6, 5, 3]
 * 执行process1：time 0+5   【3，3，6，3，3】 因为index 1和index 4 撞了，都是5，改成ceil 5/2 = 3
 * 执行process2：time 5+3      【3，6，2，3】 index1和4的3 和 index 2和5 的3 不是一开始就一样，是从之前的5改下来的，所以只有index4被改
 * 执行process3：time 8+3         【6，2，2】 index5上的3和正在执行的3撞了，需要改成ceil
 * 执行process4：time 11+6           【2，2】 这两个2也不是一开始就一样，所以他们不会被改ceil
 * 执行process5：time 17+2              【2】
 * 执行process6：time 19+2               结束  =》 total 21
 *
 * 解法：Hash map<int,int>, key是值，value是当前的值。遍历数组，每当key再出现一次，先加一次当前value，然后把当前value变为ceil(key)/2。
 */

public class Ceil {
    public static void main(String[] args) {
        Ceil ceil = new Ceil();
        int[] test1 = {4,3,3,3};
        int[] test2 = {5,5,3,6,5,3};
        int[] test3 = {5,8,4,4,8,2};
        System.out.println(ceil.getTime(test1));
        System.out.println(ceil.getTime(test2));
        System.out.println(ceil.getTime(test3));
    }

    public int getTime(int[] processes) {
        int ans = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int process : processes) {
            if (map.containsKey(process)) { // this process has been seen before, do the ceil
                // need to first cast the divisor into double for the ceil function, otherwise it's useless on int
                map.put(process, (int) Math.ceil((double) map.get(process) / 2));
            } else { // this process appears first time, can be put exactly as it is
                map.put(process, process);
            }
            ans += map.get(process); // add the reduced time to ans
        }
        return ans;
    }
}