import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Data was located at n different locations, over the years, it was moved from one server to another m times.
 * the ith operation, the data was moved from movedFrom[i] to movedTo[i]
 * Find the locations of the data after all m moving operations, return the locations in ascending order.
 *
 * i.e. locations[1,7,6,8], movedFrom[1,7,2], movedTo[2,9,5]
 * data moved 3 times: from 1->2, next from 7->9, finally from 2->5
 * in the end locations of data are: [5,6,8,9]
 */
public class MoveData {
    public static void main(String[] args) {
        int[] locations = new int[] {1,7,6,8};
        int[] movedFrom = new int[] {1,7,2};
        int[] movedTo = new int[] {2,9,5};
        MoveData test = new MoveData();
        System.out.println(Arrays.toString(test.moveData(locations, movedFrom, movedTo)));
    }
    public int[] moveData(int[] locations, int[] movedFrom, int[] movedTo) {
        Set<Integer> set = new HashSet<>();
        for (int location : locations) {
            set.add(location);
        }
        for (int i = 0; i < movedFrom.length; i++) {
            set.remove(movedFrom[i]);
            set.add(movedTo[i]);
        }
        return set.stream().mapToInt(Integer::intValue).sorted().toArray();
    }

}
