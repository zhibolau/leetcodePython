import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * there are n developers working at amazon where the ith developer has the experience points experience[i]
 * the company pay the developers with the highest and lowest remaining experience points for a hackerthon
 * The combined experience of a pair is the average of the experience points of the two developers
 * Find the number of unique values among the combined experience of the pairs formed.
 *
 * i.e: experience = [1,4,1,3,5,6], pairs are (1,6), (1,5), (4,3), experience points: 3.5, 3, 3.5
 * There are 2 distinct values 3 and 3.5, so return 2
 *
 * 先排序!!!!!再求第一个和最后一个平均值存在set里，最后看set的size
 */
public class UniqueValues {
    public static void main(String[] args) {
        UniqueValues test = new UniqueValues();
        int[] test1 = {1,4,1,3,5,6};
        int[] test2 = {1,3,4,5,6,7,7};
        int[] test3 = {1,1,3,4,4,5,6};
        System.out.println(test.findUniqueValues(test1));
        System.out.println(test.findUniqueValues(test2));
        System.out.println(test.findUniqueValues(test3));
    }
    public int findUniqueValues(int[] experiences) {
        int len = experiences.length;
        Arrays.sort(experiences);
        Set<Double> appeared = new HashSet<>();
        // if n is even number then just use i < len/2 is fine
        for(int i = 0; i <= len / 2; i++) { // if n is odd, then middle one forms a pair with itself
            // find the medium of pairs(fist, last)
            int min = experiences[i];
            int max = experiences[len - i - 1];
            double val = (double)(max + min) / 2;
            appeared.add(val);
        }
        return appeared.size();
    }
}
