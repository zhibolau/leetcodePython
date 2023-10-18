import java.util.Arrays;

/**
 * 完全不知道题是什么！！！
 */
public class SmallestPalindrome {
    public static void main(String[] args) {
        String s = "cbatabc";
        SmallestPalindrome test = new SmallestPalindrome();
        System.out.println(test.smallestPalindrome(s));
    }
    public String smallestPalindrome(String s) {
        int len = s.length();
        int halfLen = len / 2;
        StringBuilder stringBuilder = new StringBuilder();
        char[] subString = s.substring(0, halfLen).toCharArray();
        Arrays.sort(subString);
        System.out.println(Arrays.toString(subString));
        if (len % 2 == 0) {
            stringBuilder.append(s.charAt(halfLen));
        }
        for (int i = halfLen - 1; i >= 0; i--) {
            stringBuilder.append(s.charAt(i));
        }
        return stringBuilder.toString();
    }
//    public String smallestPalindrome(String s) {
//        int[] count = new int[26];
//        for (char c : s.toCharArray()) {
//            count[c - 'a']++;
//        }
//        // build first half of the string
//        char mid;
//        String ans = "";
//        for (int i = 0; i < 26; i++) {
//            String temp = count[i] / 2
//        }
//    }
}
