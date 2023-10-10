// 020 K occourrence
// given a string word, a string sequence
// if word only happens in sequence once consecutively, then we call it 1 occourrence .
// like word = “ab” and sequence = “dabcacab”, then it is a 1-occurrence.

// now we are given a sequence and a bunch of words(queries), check the k of each one of them.
// return the result in array.

public class koccurance {
    public koccurance() {
    }

    public int[] solution(String[] words, String sequence) {
        int[] res = new int[words.length];

        for(int i = 0; i < words.length; ++i) {
            int num = 0;

            for(String word = words[i]; sequence.indexOf(word) != -1; ++num) {
                word = word + words[i];
            }

            res[i] = num;
        }

        return res;
    }

    public static void main(String[] args) {
        koccurance ko = new koccurance();
        String[] words = new String[]{"ab", "babc", "bca"};
        int[] res = ko.solution(words, "aaa");

        for(int i = 0; i < res.length; ++i) {
            System.out.print(res[i]);
            System.out.print(" ");
        }

    }
}

