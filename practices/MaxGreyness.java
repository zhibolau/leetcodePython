import java.util.Arrays;

/**
 * A black and white image is composed of pixel and is represented as an n*m grid of cells, each pixel have 0 or 1.
 * 0 represents a white, and 1 represents a black.
 * the greyness of a cell(i,j) is the difference between number of black pixel in the ith row and jth column, and the number of while in ith row and jth col
 * Find the maximum greyness among all the cells of the grid
 *
 * 给一个2D array，array[i][j]表示在(i, j)点处的灰度值，0为白1为黑，(i, j)处的灰度值为第i行所有点灰度值 + 第j列所有点灰度值之和 （黑+1，白-1），求array中灰度值最大的点的灰度值
 * 按照行数给个string array，比如第一行是1 1 0 1，第二行是0 1 0 1，第三行是1 0 1 0，给的input就是{"1101","0101","1010"}
 *
 * 两层for循环‍‌分别求出colsGrey[]和 rowsGrey[]然后再遍历一遍求max即可
 *
 * i.e. 1|1|0|1
 *      0|1|0|1
 *      1|0|1|0
 */
public class MaxGreyness {
    public static void main(String[] args) {
        MaxGreyness test = new MaxGreyness();
        System.out.println(test.maxGreyNess(new String[]{"1101","0101","1010"}));
    }
    public int maxGreyNess(String[] grid) {
        int[] row = new int[grid.length];
        int[] col = new int[grid[0].length()];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length(); j++) {
                // calculate the difference between the number of (1) black and (0) white in the ith row and jth column
                if (grid[i].charAt(j) == '1') {
                    row[i] += 1; // 如果是黑，count++，如果是白，count--
                    col[j] += 1;
                } else {
                    row[i] -= 1;
                    col[j] -= 1;
                }
            }
        }
        int maxRow = Integer.MIN_VALUE;
        int maxCol = Integer.MIN_VALUE;
        for (int r : row) {
            maxRow = Math.max(maxRow, r);
        }
        for (int c : col) {
            maxCol = Math.max(maxCol, c);
        }
        return maxRow + maxCol;
    }

}
