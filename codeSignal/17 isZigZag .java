//017 isZigZag

//given an array, for each triplet, return if it is zigzag or not, and return them as the an array. 1 is zigzag 0 is not.


public class zigzagArray {
    public zigzagArray() {
    }

    public boolean[] solution(int[] array) {
        int n = array.length;
        int[] res = new int[n - 2];

        for(int i = 2; i < n; ++i) {
            int a = array[i - 2];
            int b = array[i - 1];
            int c = array[i];
            if (b > a && b > c || a > b && b < c) {
                res[i - 2] = 1;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int[] array = new int[]{1, 2, 1, 3, 1, 2, 3, 2, 3, 1};
        zigzagArray za = new zigzagArray();
        boolean[] res = za.solution(array);

        for(int i = 0; i < res.length; ++i) {
            System.out.print(res[i]);
            System.out.print(" ");
        }

    }
}

