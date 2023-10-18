import java.util.Arrays;

/**
 * given a string, categories, find the number of ways to split the string into exactly 2 contiguous non-empty substrings,
 * such that the number of distinct characters occurring in both the substring is greater than a given integer k
 * i.e.: abbcac, k=1 => 2 says of split that's > 1
 * prefix   | suffix | # shared | list of shared
 *  a       bbcac       1           a
 *  ab      bcac        2           a,b     check
 *  abb     cac         1           a
 *  abbc    ac          2           a,c     check
 *  abbca   c           1           c
 *
 *  解法：Create prefix and suffix arrays and store all the unique characters seen till now in the prefix and suffix respectively.
 *  Then for every index 'i', use a frequency array to find the count of common characters in the prefix[i] and suffix[i] respectively.
 *  If this count is greater than 'k', then this is a valid partition. So, increment the count of partitions.
 */
public class NumWaysToSplit {
    public static void main(String[] args) {
        NumWaysToSplit test = new NumWaysToSplit();
        String s = "abbcac";
        String s1 = "abdccdbada";
        String s2 = "abbddcacd";
        System.out.println(test.findNumWaysToSplit(s,1));
        System.out.println(test.findNumWaysToSplit(s1,2));
        System.out.println(test.findNumWaysToSplit(s2,1));
    }
    public int findNumWaysToSplit(String s, int k) {
        int[] prefix = new int[26];
        int[] suffix = new int[26];
        for(char c : s.toCharArray()) {
            suffix[c-'a']+=1; //abbcac => [2,2,2,0,0....] initially count of chars
        }
        int categories = 0;
        int ans = 0;
        for(int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            int idx = cur - 'a';

            int pre = prefix[idx], suf = suffix[idx];
            // when pre=0 and suf>1 means that it has the ability to move that char into left, and appear in both sub strings
            if(pre == 0 && suf > 1) categories++;
            else if (suffix[idx] <= 1) categories--;

            if(categories > k) {
                ans++;
            }
            prefix[idx]++;
            suffix[idx]--;
        }
        return ans;
    }
}
