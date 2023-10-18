import java.util.ArrayList;
import java.util.List;

/**
 * Given a string, split the string into 2 substrings at every possible point, the rightmost substring is a suffix.
 * the beginning of the string is the prefix. Determine the length of the common prefix between each suffix and the original string.
 * Sum and return the lengths of the common prefixes. Return an array where each element i is the sum for string i.
 *
 * i.e. abcabcd => sum = 7+3 = 10
 * remove |  suffix | common prefix | length
 * "        abcabcd     abcabcd         7
 * a        bcabcd
 * ab       cabcd
 * abc      abcd        abc             3
 * abca     bcd
 * abcab    cd
 * abcabc   d
 */
public class CommonPrefix {
    public static void main(String[] args) {
        String s = "abcabcd";
        CommonPrefix test = new CommonPrefix();
        System.out.println(test.findCommonPrefix(s));
    }
    public int findCommonPrefix(String s) {
        List<Integer> counts = new ArrayList<>();
        int ans = s.length(); // base case where the string is split to " and itself
        for (int i = 0; i < s.length() - 1; i++) { // from 0 to second last char
            int currentLen = 0;
            for (int j = i + 1; j < s.length(); j++) { // from i+1 to last char
                // abcabcd, i=0,j=1,j-i-1=0, break; i=2,j=3,4,5 => (abc, abcd) j-i-1= 0,1,2
                if (s.charAt(j - i - 1) == s.charAt(j)) {
                    currentLen++;
                } else break;
            }
            counts.add(currentLen);
        }
        for (int count : counts) ans += count;
        return ans;
    }
}
