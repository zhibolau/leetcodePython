import java.util.Arrays;

/**
 * Take the new password, choose a set of indices and change the characters at these indecies to the next cyclic char exactly once
 * Char a is changed to b, b changed to c... and z changed to a
 * The password is similar if after applying this operation, the old password is a subsequence of the new password
 * For each pair of old/new passwords, return yes if new[i] is a subsequence of old[i], and no otherwise
 * i.e:
 * newPasswords = ["baacbab", "accdb", "baacba"]
 * oldPasswords = ["abdbc", "ach", "abb]
 * ba|ac|ba|b => change ac to bd, last b to c => babdbac => b(abdb)a(c) 括号里的和old abdbc一样，所以是YES
 *
 * 换password，对于新的password做a->b, b->c, c->d, z->a的处理，然后看新的password是不是旧的substr
 *
 */
public class NewPassword {
    public static void main(String[] args) {
        NewPassword test = new NewPassword();
        String[] newPs = {"baacbab","accdb","baacba"}; //baacba => ba|a|cba => babcba,包含abb, 第三个true
        String[] olePs = {"abdbc","ach","abb"};
        String[] ans = test.similarPassword(olePs, newPs);
        System.out.println(Arrays.toString(ans));
    }
    private char transform(char c) {
        if (c == 'z') return 'a';
        return c += 1;
    }
    private boolean isSubString(String newStr, String oldStr) { //判断oldString是不是newStr的sub string
        if (oldStr.length() > newStr.length()) return false;
        int oldPtr = 0, newPtr = 0;
        while (newPtr < newStr.length() && oldPtr < oldStr.length()) {
            char newChar = newStr.charAt(newPtr);
            char oldChar = oldStr.charAt(oldPtr);
            if (oldChar == newChar || transform(newChar) == oldChar) oldPtr++;
            newPtr++;
        }
        return oldPtr == oldStr.length();
    }
    public String[] similarPassword(String[] oldPasswords, String[] newPasswords) {
        int len = newPasswords.length;
        String[] ans = new String[len];
        for (int i = 0; i < len; i++) {
            String oldPass = oldPasswords[i];
            String newPass = newPasswords[i];
            ans[i] = isSubString(newPass, oldPass) ? "YES" : "NO";
        }
        return ans;
    }
}
