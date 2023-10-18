import java.util.Arrays;

/**
 * array starting with one, adjacent value should have difference <=1
 * 给一个数组，num[0]永远是1， 所有数组内数字的差值需 <= 1， 如果超过了1 大的数字可以随意减小到 <= 1。求该数组能有的最大值。
 */
public class GetMaxValue {
    public static void main(String[] args) {
        GetMaxValue test = new GetMaxValue();
        System.out.println(test.maximumElementAfterDecrementingAndRearranging(new int[]{2, 6, 4, 1}));
    }
    public int maximumElementAfterDecrementingAndRearranging(int[] array) {
        Arrays.sort(array);
        array[0] = 1;
        for (int i = 1; i < array.length; i++) {
            if (array[i] > array[i - 1] + 1) {
                array[i] = array[i - 1] + 1;
            }
        }
        return array[array.length - 1];
    }
}
