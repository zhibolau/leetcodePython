import java.util.HashSet;
import java.util.Set;

/**
 * 分割字符串,每个字符串无重复 minimum redundancy-free segments
 * i.e:"a|abcde|a": 3
 * "al|ab|a|ma":4
 * "a|a|a|a|a|a":6
 */
public class MinSegments {
    public static void main(String[] args) {
        MinSegments test = new MinSegments();
        System.out.println(test.minSegments("alabama"));
    }
    public int minSegments1(String s) { // 但是会开辟很多count数组
        int[] count = new int[26];
        int ans = 0;
        for(char c : s.toCharArray()) {
            if(count[c - 'a'] > 0) { //curr seg里面已经有了这个char了，需要重新开一个
                ans++;
                count = new int[26];
            }
            count[c - 'a']++; //还没有，increment count
        }
        return ans + 1;
    }
    public int minSegments(String s) {
        if (s == null || s.length() == 0) return 0;
        int right = 0, ans = 1;
        Set<Character> set = new HashSet<>();
        while (right < s.length()) {
            if (set.contains(s.charAt(right))) {
                set.clear();
                ans++;
            }
            set.add(s.charAt(right++));
        }
        return ans;
    }
}
