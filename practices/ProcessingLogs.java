import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 交易日志处理 返回超过阈值的用户ID
 */
public class ProcessingLogs {
    public static void main(String[] args) {

    }
    public List<String> processLog(List<String> logs, int k) {
        List<String> result = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        for (String log : logs) {
            StringBuilder s1 = new StringBuilder();
            StringBuilder s2 = new StringBuilder();
            int space = 0;
            for (int i = 0; i < log.length(); i++) {
                if (log.charAt(i) == ' ') space++;
                else if (space == 0) s1.append(log.charAt(i));
                if (space == 1) s2.append(log.charAt(i));
                else break;
            }
        }
        return null;
    }
}
