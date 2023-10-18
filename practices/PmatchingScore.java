import java.util.Map;

/**
 * p-matching score: prevent customers from having very similar usernames
 * consider 2 user ID: username1 with len n and username2 with len m. => string of lowercase english letter
 * P-matching score: maximum number of distinct indicies i such that the string formed by concating
 * char username1[i], username1[i+p]..., username1[i + (m-1) * p] can be rearranged to username2
 * where 0 <= i; i + (m-1)*p < n; i <= p
 * <p>
 * i.e. username1 = "acaccaa", username2 = "aac" , p=2
 * i = 0, i+=p = 2, new String: u1[0] + u1[2] + u1[4] = aac => m=3,所以index 0只加两个 => equal username2, valid
 * i = 1, i+=p = 3, new String: u1[1] + u1[3] + u1[5] = cca => 即使rearrange也！=username2, invalid
 * i = 2, i+=p = 4, new String: u1[2] + u1[4] + u1[6] = aca => rearranged to aac => valid
 * 因为有2个valid indices，return2
 */
public class PmatchingScore {
    public static void main(String[] args) {
        PmatchingScore test = new PmatchingScore();
        System.out.println(test.getpMatchingScore("acaccaa", "aac", 2));
        System.out.println(test.getpMatchingScore("abdcacdaa", "dac", 3));
    }

    public int canRearrange(String s1, String s2) { // if rearrange is same => 1, not same => 0
        if (s1.length() != s2.length()) return 0;
        int[] counts = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            counts[s1.charAt(i) - 'a']++;
            counts[s2.charAt(i) - 'a']--;
        }
        for (int count : counts) {
            if (count != 0) return 0;
        }
        return 1;
    }
    public int getpMatchingScore(String username1, String username2, int p) {
        int count = username2.length(); // 要加字母的次数
        int start = 0;
        int ans = 0;
        while (start + (count - 1) * p < username1.length()) { // 从index start开始，且加上m次仍在len1范围内
            StringBuilder sb = new StringBuilder();
            int index1 = start;
            while (count > 0) {
                sb.append(username1.charAt(index1)); //构造newString，并且向下移动p个单位，count--
                index1 += p;
                count--;
            }
            System.out.println(sb);
            ans += canRearrange(username2, sb.toString());
            count = username2.length(); //复位 count
            start++;
        }
        return ans;
    }
}
