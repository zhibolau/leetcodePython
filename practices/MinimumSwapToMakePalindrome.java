/**
 * Give a binary string consisting of 0’s and 1’s only. E.g., 0100101. We are allowed to pick
 * any two indexes and swap them. We have to return the minimum number of swaps required to make
 * it a palindrome or -1 if it cannot. The string 0100101 can be made a palindrome by swapping
 * (3,4)-> 0101001 and swapping (0,1) -> 1001001 which is a palindrome. In this case, the
 * correct answer is 2.
 *
 * You could compare the outermost two digits:
 * if they are the same, nothing needs to happen, nor should these digits ever be involved in a swap.
 * If they are different, take note of that, and don’t swap anything yet.
 *
 * Continue with the second digit at each end. Compare them.
 * If they are different, and this is the second time we have a difference, note how we can solve those two differences with one swap. An example:
 *  10.......10
 * With one swap this can become:
 *  10.......01
 * So we can resolve two differences with one swap. This means that if we find and even number of differences — as we walk along the binary string from the two ends inwards — there is a solution, and it takes half that number of swaps.
 *
 * If the number of differences is odd, there is still a solution if the input string is odd,
 * because then that middle digit can be swapped with a digit from that last difference, and so get a palindrome.
 *
 * There is however no solution when the number of differences (in this algorithm) is odd and the number of digits in the input is even.
 */
public class MinimumSwapToMakePalindrome {
    public static void main(String[] args) {
        MinimumSwapToMakePalindrome test = new MinimumSwapToMakePalindrome();
        System.out.println(test.swapPalindrome("0100101")); //0100101 首位末尾，第二位到第二不一样，swap，然后中间和4 index swap
    }
    public int swapPalindrome(String s) {
        int count = 0;
        int len = s.length();
        for (int i = 0; i < len / 2; i++) {
            if (s.charAt(i) != s.charAt(len - i - 1)) count++;
        }
        if (count % 2 == 1 && len % 2 == 0) return -1;
        return (count + 1) / 2;
    }
}
