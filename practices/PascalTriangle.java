import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * When an array of digits is fed to this system, it sums the adjacent digits.
 * it then takes the rightmost digit (LSD) of each addition for the next step
 * thus, the number of digits in each step is reduced by 1.
 * This procedure is repeated until there are only 2 digits left, and the sequence of 2 digits forms the encrypted number
 * Given the initial sequence of digits, return a string of teh entrypted number.
 *
 * i.e.: [4,5,6,7] => sum each and only take 个位数: [9,1,3] =>[0,4] => 04
 */
public class PascalTriangle {
    public static void main(String[] args) {
        PascalTriangle test = new PascalTriangle();
        System.out.println(test.getEncryptedNumber(new int[]{1,2,3,4,5}));
    }
    public String getEncryptedNumber(int[] numbers) {
        int len = numbers.length;
        // 因为是倒三角，所以直接在愿数组从后往前替换，前面的元素其实没有被覆盖
        // 1，2，3，4，5
        //    3，5，7，9
        //       8，2，6
        //          0，8
        for (int i = 0; i < len - 2; i++) { // i代表row 从0到倒数第二行
            for (int j = len - 1; j > i; j--) { // j从后往前，代表要替换的index
                numbers[j] = (numbers[j] + numbers[j - 1]) % 10; //前一行的两个数相加取个位，赋值到当前行
            }
        }
        return numbers[len-2] + "" + numbers[len-1]; // 数组的最后两位数就是答案
    }
}
