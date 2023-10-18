import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * 一个密码段如果同时含有至少一个元音和一个辅音， 称这个密码是strong的
 * 给定一个密码，问这个密码的强壮度（每含有上述一个密码段强壮度+1）
 * input "thisisbeautiful"
 * output 6
 * explain: thi si sbe aut if ul
 */
public class PasswordStrength {
    public static void main(String[] args) {
        PasswordStrength test = new PasswordStrength();
        System.out.println(test.passwordStrength("thisisbeautiful"));
    }
    public int passwordStrength(String s) {
        int ans = 0;
        Set<Character> yuan = new HashSet<>(Arrays.asList('a', 'e', 'i','o','u'));
        boolean isYuan = false, isFu = false;
        for (char c : s.toCharArray()) {
            if (yuan.contains(c)) isYuan = true;
            else isFu = true;
            if (isYuan && isFu) {
                ans++;
                isFu = false;
                isYuan = false;
            }
        }
        return ans;
    }
}
