/**
 * 根据指令上下左右移动，返回最终位置
 */
public class RiverControl {
    public static void main(String[] args) {
        RiverControl test = new RiverControl();
        System.out.println(test.riverControl(new String[]{"RIGHT", "DOWN", "LEFT", "LEFT", "DOWN"}, 4));
    }
    public int riverControl(String[] cmds, int n) {
        // move in a n * n matrix
        int row = 0, col = 0;
        for (String cmd : cmds) {
            if (cmd.equals("UP") && row > 0) {
                row--;
            }
            if (cmd.equals("DOWN") && row < n - 1) {
                row++;
            }
            if (cmd.equals("LEFT") && col > 0) {
                col--;
            }
            if (cmd.equals("Right") && col < n - 1) {
                col++;
            }
        }
        return row * n + col;
    }
}
