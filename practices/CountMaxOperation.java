import java.util.HashMap;
import java.util.Map;

/**
 * given a log entry s and target word t, the target word can be obtained by selecting some subset of char from s,
 * that can be rearranged to form string t and removing them from s.
 * Determine the maximum number of times the target word can be removed from the given log entry
 *
 * i.e.: s="mononom", t="mon" => 2
 * 给两个字符串s和t，求问使用s所有的字母最多能够重组出几个t。思路是用两个hashmap统计s和t的字母出现频率，
 * 然后遍历t的所有字母，找到s中出现次数/t中出现次数的最小值（向下取整）
 */
public class CountMaxOperation {
    public static void main(String[] args) {
        CountMaxOperation test = new CountMaxOperation();
        String s = "mononom";
        String t = "mon";
        System.out.println(test.countMaximumOperations(s, t));
    }
    public int countMaximumOperations(String s, String t) {
        int ans = Integer.MAX_VALUE;
        // keep track of the occurrences for each character in s and t
        Map<Character, Integer> mapS = new HashMap<>();
        Map<Character, Integer> mapT = new HashMap<>();
        for (char ch : s.toCharArray()) {
            mapS.put(ch, mapS.getOrDefault(ch,0) + 1);
        }
        for (char ch : t.toCharArray()) {
            mapT.put(ch, mapT.getOrDefault(ch, 0) + 1);
        }
        // traverse each character in t
        for (char ch : t.toCharArray()) {
            int count = mapS.getOrDefault(ch, 0) / mapT.get(ch);
            ans = Math.min(count, ans);
        }
        return ans;
    }
}
