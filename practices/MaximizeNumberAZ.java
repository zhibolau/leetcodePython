/**
 * Given a string consisting of uppercase English letters, at most one char can be added anywhere in the string
 * Add at most 1 uppercase char to maximize the number of "AZ" subsequences
 * subsequence: deleting chars while maintain th original order SAKZ -> AZ
 * i.e.: s="AKZ", add "A" after K to make AKAZ, the # of subsequence AZ is 2
 *
 * 思路：
 * A肯定要加在开头才能尽可能多的和后面的Z组成AZ，Z肯定要加在最后才能尽可能多的和前面的A组成AZ。
 * 所以要比较的就是A+string和string+Z两种情况。然后就是数有多少个AZ。
 * 从前往后遍历新的string，每遇到一个Z，这个Z就能和前面n个A组成n个AZ，所以就是要记录到这个Z为止，总共有多少个A -> 如果不改动char。
 * 遍历结束后看A多还是Z多，总数再加上两者较大的就得到答案了。
 */
public class MaximizeNumberAZ {
    public static void main(String[] args) {
        String s = "AKZAPPP"; // 当前有一个AZ，A：2，Z：1, 因为A的数量多，就在结尾加上Z，获取两个AZ，一共3个
        MaximizeNumberAZ test = new MaximizeNumberAZ();
        System.out.println(test.maximizeNumber(s));
    }
    public int maximizeNumber(String s) {
        int nA = 0, nZ = 0, ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'A') nA++;
            if (s.charAt(i) == 'Z') {
                ans += nA;
                nZ++;
            }
        }
        ans += Math.max(nA, nZ); //如果A多就在结尾加Z，z多就在开头加A
        return ans;
    }
}
