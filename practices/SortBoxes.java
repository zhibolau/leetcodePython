import java.util.*;

/**
 * some boxes have already been upgraded, and other boxes have not.
 * identify the oldest boxes that need to be upgraded first but leaving the newer model boxes, so they won't be prioritized
 * All boxes are identified by an alphanumeric identifier, followed by space delimited version info.
 * older generation uses space delimited lowercase English strings to identify the version
 * newer generation uses space delimited positive integers to identify the version
 * <p>
 * task: sort:
 * 1.older generation  should be returned first, sorted by lexicographic order
 * 2.ties should be broken by alphanumeric identifier
 * 3.newer generation mustt all come after older, in the original order they were given
 * <p>
 * i.e. input = [ykc 82 01],[eo first qpx],[09z cat hamster],[06f 12 25 6],[az0 first qpx],[236 cat dog rabbit snake]
 * output=[263 cat dot rabbit snake], [09z cat hamster],[az0 first qpx],[eo first qpx], [ykc 82 01],[06f 12 25 6]
 */
public class SortBoxes {
    public static void main(String[] args) {
        SortBoxes test = new SortBoxes();
        System.out.println(test.sortBoxes(Arrays.asList("ykc 82 01", "at first qpx","eo first qpx", "az first qpx","09z cat hamster", "06f 12 25 6", "az0 first qpx", "236 cat dog rabbit snake")));
    }

    public List<String> sortBoxes(List<String> boxList) {

        //variables and checking input
        if (boxList == null) return null;
        int boxListSize = boxList.size();
        if (boxListSize < 1) return boxList;
        List<String> result = new ArrayList<>();

        //add older junction boxes to result list
        int firstSpace;
        for (String s : boxList) {
            firstSpace = s.indexOf(" ");
            if (!Character.isDigit(s.charAt(firstSpace + 1))) { //如果空格后的第一位不是数字，old，加入
                result.add(s);
            }
        }

        //sort older junction boxes with comparator in result list
        result.sort((s1, s2) -> {

            String substring1 = s1.substring(s1.indexOf(" ") + 1); // 只要第一个空格后的对比，如果一样，再比较前面的
            String substring2 = s2.substring(s2.indexOf(" ") + 1);
            if (substring1.equals(substring2)) {
                //set substrings to alphanumeric identifier to compare the identifier instead
                substring1 = s1.substring(0, s1.indexOf(" "));
                substring2 = s2.substring(0, s2.indexOf(" "));
            }

            int minLength = Math.min(substring1.length(), substring2.length());
            for (int i = 0; i < minLength; i++) {
                if (substring1.charAt(i) < substring2.charAt(i)) return -1;
                if (substring1.charAt(i) > substring2.charAt(i)) return 1;
            }

            return substring1.length() - substring2.length();

//            if (minLength == substring1.length() && minLength == substring2.length()) {
//                return 0;
//            } else if (minLength == substring1.length()) {
//                return -1;
//            } else {
//                return 1;
//            }

        });

        //iterate through original list and add newer junction boxes to result list
        for (String s : boxList) {
            firstSpace = s.indexOf(" ");
            if (Character.isDigit(s.charAt(firstSpace + 1))) {
                result.add(s);
            }
        }
        return result;
    }
}
