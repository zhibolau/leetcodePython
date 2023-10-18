import java.util.Arrays;

/**
 * the positions of n data centers and n servers are given in the form of arrays,
 * any particular data center, center[i] can deliver to any particular destination[j]
 * The lag is defined distance between a data center at location x and a server destination at location y is |x-y|
 * Determine the minimum lag to establish the entire network
 *
 */
public class MinimumTotalLag {

    public int minimumLag(int[] center, int[] destination) {
        int N = center.length;
        Arrays.sort(center);
        Arrays.sort(destination);
        int minLag = 0;
        for(int i = 0; i < N; i++) {
            minLag += Math.abs(destination[i] - center[i]);
        }
        return minLag;
    }
}
