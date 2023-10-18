import java.util.LinkedList;
import java.util.Queue;

/**
 * You want to find the shortest path to arrive at any food cell.
 * You are given an m x n character matrix, grid, of these different types of cells:
 *
 * '*' is your location. There is exactly one '*' cell.
 * '#' is a food cell. There may be multiple food cells.
 * 'O' is free space, and you can travel through these cells.
 * 'X' is an obstacle, and you cannot travel through these cells.
 * You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.
 *
 * Return the length of the shortest path for you to reach any food cell.
 * If there is no path for you to reach food, return -1.
 */

//Time Complexity: O(MN)
//Space Complexity: O(1) 也有说法是O（MN）
// queue size is constant space because you can only choose from 4 directions in every iteration
public class ShortestPathGetFood {
    public static void main(String[] args) {

    }
    public int getFood(char[][] grid) {
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '*') {
                    queue.offer(new int[] {i, j});
                }
            }
        }
        int[][] dirs = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        int step = 1; // default step, even if we right next to food, we need one step to reach
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                for (int[] dir : dirs) {
                    // compute new coordinates
                    int x = curr[0] + dir[0];
                    int y = curr[1] + dir[1];
                    // if not valid , skip
                    if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == 'X') {
                        continue;
                    }
                    if (grid[x][y] == '#') { // found food, can return
                        return step;
                    }
                    grid[x][y] = 'X'; //set it to be a wall to indicate visited
                    queue.offer(new int[] {x, y});
                }
            }
            step++;
        }
        return -1;
    }
}
