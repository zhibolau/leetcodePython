import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Given an array of integers, determine the number of distinct subarrays that can be formed having at most a given number of odd elements.
 * (number of distinct subarrays having at most k odd elements).
 * [1,1,2,3] -> 112,123,13,12,11,1,23,3,2
 */
public class NumOfSubarrayWithKoddNumbers {
    public static void main(String[] args) {
        NumOfSubarrayWithKoddNumbers test = new NumOfSubarrayWithKoddNumbers();
        System.out.println(test.countSubarray(new int[]{1,1,2,3}, 2));
    }

    public int countSubarray(int[] nums, int k) {
        StringBuilder stringBuilder = new StringBuilder();
        Set<String> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            stringBuilder.setLength(0);
            int oddCount = 0;

            for (int j = i; j < nums.length; j++) {
                if (nums[j] % 2 != 0) oddCount++;
                if (oddCount > k) break;
                stringBuilder.append("{").append(nums[j]).append("}");
                set.add(stringBuilder.toString());
            }
        }
        System.out.println(set);
        return set.size();
    }
}

