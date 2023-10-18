/**
 * A word a is said to be transformable to a word b if a is a subsequence of b.
 * Given searchWord and resultWord, find the minimum number of characters that must be appended at the end of the searchWord,
 * such that resultWord is a subsequence of teh modified searchWord => subsequence: 可以删除，不可以改变位置
 * i.e.: searchWord = "armaze"
 *       resultWord = "amazon"
 *       (a)r(maz)e -> (a)r(maz)e(o) -> (a)r(maz)e(on) => amazon
 *      add 2 chars "on" to searchWord to make resultWord a subsequence of searchWord => return 2
 *
 * 解法：使用双指针ps pr分别遍历字符串，如果指向的字符相同，则双指针同时向后移动，反之只移动ps，知道任意指针到达结尾
 * 返回resultString的长度与pr指针位置的差
 */
public class SearchWord {
    public static void main(String[] args) {
        SearchWord test = new SearchWord();
        System.out.println(test.searchWordToResultWord("armaze", "amazon"));
    }
    public int searchWordToResultWord(String searchWord, String resultWord) {
        int ps = 0, pr = 0;
        while(ps < searchWord.length() && pr < resultWord.length()) {
            if(searchWord.charAt(ps) == resultWord.charAt(pr)) {
                pr++;
            }
            ps++;
        }
        return resultWord.length() - pr;
    }
}
