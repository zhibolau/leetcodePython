import java.util.Arrays;

/**
 * You have a keypad with 9 buttons, numbered from 1-9, each mapped to lowercase English letters.
 * You can choose which characters each button is matched to as long as:
 * • All 26 lowercase English letters are mapped to.
 * • Each character is mapped to by exactly 1 button.
 * • Each button maps at most 3 characters.
 * To type the first character that matched to a button, you press the button once.
 * To type the second character, you press the button twice, and so on.
 * Given a string s, return the minimum number of keypresses needed to type s using your keypad.
 */
public class KeypadClick {
    public static void main(String[] args) {

    }
    public int minimumKeyPress(String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        Arrays.sort(count); // 每个char按照出现次数从小到大排列
        int ans = 0, press = 1, usedNum = 0; //default先按一次
        for (int i = 25; i >= 0; i--) { //从后往前遍历，因为后面的出现次数多，排在前面按次数就少
            if (count[i] == 0)
                continue;
            ans += count[i] * press;
            usedNum++;
            if (usedNum == 9) {
                usedNum = 0; // 已经超过9个了，就需要按两次
                press++;
            }
        }
        return ans;
    }
}
