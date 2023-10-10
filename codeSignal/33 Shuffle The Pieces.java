// given two arrays, arr and pieces
// arr is a one dimension array
// and pieces is a higher dimension array.

// example:
// arr: [1,2,5,3]
// pieces = [[5],[1,2],[3]]

// and we need to write a function to check whether if we only all the pieces can we form an original arr.
// ————————————————


public class ShuffleThePieces {
    public ShuffleThePieces() {
    }

    public int[] solution(int[][] arraies, int[] path) {
        Map<Integer, Integer> map = new HashMap();
        Map<Integer, Integer> mapB = new HashMap();

        for(int i = 0; i < path.length; ++i) {
            map.put(path[i], 0);
            mapB.put(path[i], 0);
        }

        int[][] var11 = arraies;
        int var6 = arraies.length;

        int start;
        int key;
        for(start = 0; start < var6; ++start) {
            int[] array = var11[start];
            if ((Integer)map.get(array[1]) == 1 || (Integer)mapB.get(array[0]) == 1) { //we can compare Integer to int directly.
                key = array[1];
                array[1] = array[0];
                array[0] = key;
            }

            map.put(array[1], 1);
            mapB.put(array[0], 1);
        }

        int[] res = new int[path.length];
        Map<Integer, Integer> trace = new HashMap();
        int[][] var14 = arraies;
        int index = arraies.length;

        for(key = 0; key < index; ++key) {
            int[] array = var14[key];
            trace.put(array[0], array[1]);
        }

        start = 0;
        Iterator var16 = map.keySet().iterator();

        while(var16.hasNext()) {
            key = (Integer)var16.next();
            if ((Integer)map.get(key) == 0) {
                start = key;
            }
        }

        for(index = 0; trace.containsKey(start); ++index) {
            res[index] = start;
            start = (Integer)trace.get(start);
        }

        res[index] = start;
        return res;
    }

    public static void main(String[] args) {
        int[][] arries = new int[][]{{3, 1}, {5, 3}, {5, 7}, {7, 4}, {9, 4}};
        int[] path = new int[]{1, 3, 5, 7, 4, 9};
        ShuffleThePieces st = new ShuffleThePieces();
        int[] res = st.solution(arries, path);

        for(int i = 0; i < res.length; ++i) {
            System.out.print(res[i]);
            System.out.print(" ");
        }

    }
}

