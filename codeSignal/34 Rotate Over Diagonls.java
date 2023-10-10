// 034 Rotate Over Diagonls
// the picture above is the process of rotating.

// codes in java:

public class rotateOverDigonals {
    public rotateOverDigonals() {
    }

    public void solution(int[][] matrix, int k) {
        if (matrix.length != 0 && matrix != null) {
            k %= 4;

            for(int i = 0; i < k; ++i) {
                this.rotate(matrix);
            }

        }
    }

    public void rotate(int[][] matrix) {
        int rightdiagonal = matrix.length - 1;

        int i;
        for(i = 0; i < matrix.length; ++i) {
            for(int j = i; j < matrix[0].length; ++j) {
                if (j != rightdiagonal) {
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = temp;
                }
            }

            --rightdiagonal;
        }

        for(i = 0; i < matrix.length; ++i) {
            this.reverse(matrix[i], 0, matrix.length - 1, i, matrix.length - 1 - i);
        }

    }

    public void reverse(int[] matrix, int start, int end, int leftdigonal, int rightdigonal) {
        if (start < end) {
            for(int i = 0; i < (start + end) / 2; ++i) {
                if (i != leftdigonal && matrix.length - i - 1 != rightdigonal && i != rightdigonal && matrix.length - i - 1 != leftdigonal) {
                    int temp = matrix[i];
                    matrix[i] = matrix[matrix.length - 1 - i];
                    matrix[matrix.length - 1 - i] = temp;
                }
            }

        }
    }

    public static void main(String[] args) {
        rotateOverDigonals rd = new rotateOverDigonals();
        int[][] matrix = new int[][]{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}};
        rd.solution(matrix, 1);

        for(int i = 0; i < matrix.length; ++i) {
            for(int j = 0; j < matrix[0].length; ++j) {
                System.out.print(matrix[i][j]);
                System.out.print(",");
            }

            System.out.print("\n");
        }

    }
}


