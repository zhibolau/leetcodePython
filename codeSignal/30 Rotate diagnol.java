030 Rotate diagnol
The problem describes it in a subtle way, so it’s better to just give answers:
more detailed explainations will be showed later

public class rotatediagnol {
    public void solution(int[][] matrix, int k){
        if(matrix == null || matrix.length == 0) return ;
        int m = matrix.length;
        int n = matrix[0].length;
        while(k>0) {
            for (int i = 0; i < m; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (i != j && i != n-1 - j) {
                        swap(matrix, i, j, j, i);
                    }
                }
            }

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n / 2; j++) {
                    if (i != j && i != n-1 - j) {
                        swap(matrix, i, j, i, n -1- j);
                    }
                }
            }
            k--;
        }

    }

    private void swap(int[][] matrix, int i, int j, int x, int y){
        int temp = matrix[i][j];
        matrix[i][j] = matrix[x][y];
        matrix[x][y] = temp;
    }

    public static void main(String[] args){
        rotatediagnol rd = new rotatediagnol();
        int[][] matrix = new int[][]{{1,2,3,4,5}, {6,7,8,9,10}, {11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};
        rd.solution(matrix, 61);
        for(int i=0; i<matrix.length; i++){
            for(int j=0; j<matrix[0].length; j++){
                System.out.print(matrix[i][j]);
                System.out.print(" ");
            }
            System.out.print("\n");
        }

    }


}

