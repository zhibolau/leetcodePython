import java.util.*;

/**
 * Amazon has a string of categories of items purchased by a particular customer, each represented as a lowercase English Letter.
 * To analyze customer behavior we define a metric called the MaximaCount of a category c is the maximum among all categorys is defined as the number of indices i such taht
 * the frequency of char is maximum in the prefix of the string up to the index i given the string categories, find the maximum MaximaCount amoung all the categories
 *
 * Given categories = "bccaaacb" there are three categories [a,b,c]
 * MaximaCount of a = 4 at indices 5,6,7,8
 * MaximaCount of b = 2 at indices 1,2
 * MaximaCount of c = 6 at indices 2,3,4,5,7,8
 *
 * complete the findMaximumMaximaCount in the edior below the function returs an integer denoting the maximum attainable favourabilit
 *
 * categories = adbcbcbcc
 * out = 6
 *
 * the string categories consists of lorcase english characters only.
 */

public class MaximumMaximaCount2 {
    static class Pair {
        int frequency;
        char aChar;
        public Pair(int frequency, char aChar) {
            this.frequency = frequency;
            this.aChar = aChar;
        }
    }
    public static int MaxiumCount(String s) {
        PriorityQueue<Pair> priorityQueue = new PriorityQueue<>(((a, b) -> b.frequency - a.frequency)); // to get the max frequency char
        Map<Character, Integer> map = new HashMap<>(); // freequency of each char
        Map<Character, Integer> maxima = new HashMap<>(); // maxima
        Map<Integer, Set<Character>> freq = new HashMap<>(); // store all chars with same frequency

        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                Set<Character> set = freq.get(map.get(c));
                set.remove(c);
                freq.put(map.get(c), set);
            }
            map.put(c, map.get(c) + 1);
            freq.get(map.get(c)).add(c);
            priorityQueue.offer(new Pair(map.get(c), c));
            int val = priorityQueue.peek().frequency;
            for (char y : freq.get(val)) {
                maxima.put(y, maxima.getOrDefault(y, 0) + 1);
            }
        }
        int ans = 0;
        for (int value : maxima.values()) {
            ans = Math.max(ans,value);
        }
        return ans;
    }
    public static void main(String[] args) {
        System.out.println(MaxiumCount("adbcbcbcc"));
    }
}
