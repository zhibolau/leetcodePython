import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * 给size为n的数组。数组里的数为n的permutation，比如[4, 1, 3, 2]。假设有个子数组s，定义该子数组imbalance计算方法子数组排序后s[i]-s[i-1] > 1的总个数。
 * 要求输出所有子数组imbalance的总个数
 *
 * 比如[4, 1, 3, 2]
 * 子数组 4 => 排序后4，imbalance = 0
 * 子数组 1 => 排序后1，imbalance = 0
 * 子数组 3 => 排序后3，imbalance = 0
 * 子数组 2 => 排序后2，imbalance = 0
 * 子数组 4,1 => 排序后1,4，imbalance = 1 因为 4-1=3>1
 * 子数组 1,3 => 排序后1,3，imbalance = 1 因为 3-1=2>1
 * 子数组 3,2 => 排序后2,3，imbalance = 0 因为 3-2=1=1
 * 子数组 4,1,3 => 排序后1,3,4，imbalance = 1 因为 3-1=2>1,4-3=1=1
 * 子数组 1,3,2 => 排序后1,2,3，imbalance = 0 因为 2-1=1=1,3-2=1=1
 * 子数组 4,1,3,2 => 排序后1,2,3,4，imbalance = 0 因为 2-1=1=1,3-2=1=1,4-3=1=1
 * 最后输出结果为3
 *
 * 解法：使用单调栈时空均为On：left-> left[i] 是i往左走第一个比i大的数的index，right -> right[i]是第一个比i大的数字
 * 创建一个value -> index的数组
 * 遍历nums，假设当前数是smaller one in imbalance，计算所有可能的subarray with it as the smaller one
 * the larger one既可以在左也可以在右，并且不能只比它大1，并且每个case要考虑在左和在右两方面
 * https://github.com/gcheng9430/InterviewPrep/blob/9995841be14ac50211174dc2a2c84d31e770e716/Guo/9.py
 * https://leetcode.com/discuss/interview-question/2461490/Amazon-OA-or-Group-Imbalance-or-2022
 */

public class FindImBalance {

    public static void main(String[] args) {
        FindImBalance test = new FindImBalance();
        int[] testArr = {4, 1, 3, 2};
        System.out.println(test.imbalanceCount(testArr));
    }

    public int imbalanceCount(int[] nums) {
        int len = nums.length;
        int[] indexArray = new int[len + 1];
        for (int i = 0; i < len; i++) { // nums: 4,1,3,2 数字4在index0上，1在index1上 -> indexArray：【0，1，3，2，0】
            indexArray[nums[i]] = i; // create value to index array [0,1,3,2,0]
        }

        int[] left = new int[len], right = new int[len];
        int[] maxStack = new int[len]; // maxStack,栈中的元素按递减顺序排列, to find first larger element on the left
        int index = -1;
        for (int i = 0; i < len; i++) { // from left to right
            // second iteration => index=0,i=1, maxStack=[0,0,0,0], nums[0]=4 > nums[1]=1, left=[-1,0,0,0]
            // third iteration => index=1,i=2, maxStack[0,1,0,0], nums[1]=1 < nums[2]=3, index-- = 0, 继续while,不符合
            while (index >= 0 && nums[maxStack[index]] < nums[i]) {
                index--;
            }
            left[i] = index < 0 ? -1 : maxStack[index]; // final left: -1,0,0,2
            index++;
            maxStack[index] = i; //i=0, index
        }

        index = -1;
        for (int i = len - 1; i >= 0; i--) { // from right to left
            while (index >= 0 && nums[maxStack[index]] < nums[i]) {
                index--;
            }
            right[i] = index < 0 ? len : maxStack[index]; // final right: 4,2,4,4
            index++;
            maxStack[index] = i;
        }

        int count = 0;
        for (int i = 0; i < len; i++) {
            if (nums[i] < len - 1) { //n自己和n-1都不可能作为imbalance里更小的那个
                int addOneIdx = indexArray[nums[i] + 1]; //find out curr+1 to avoid including it
                if (addOneIdx > i) { //if the element one larger is on the right
                    //add all possibilities of (curr,largerOnTheRight) as imbalance
                    count += (i + 1) * (addOneIdx - right[i]);
                    //add all possibilities of (largerOnTheLeft,curr) as imbalance
                    if (left[i] >= 0) {
                        count += (left[i] + 1) * (right[i] - i);
                    }
                } else { // if the element one larger is on the left
                    //add all possibilities of (largerOnTheLeft,curr) as imbalance
                    count += (left[i] - addOneIdx) * (len - i);
                    if (right[i] < len) {
                        //add all possibilities of (curr,largerOnTheRight) as imbalance
                        count += (i - left[i]) * (len - right[i]);
                    }
                }
            }
        }
        return count;
    }
}