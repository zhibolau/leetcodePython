import java.util.*;

/**
 * pick song with total time = ride duration - 30
 * The function is expected to return an INTEGER_ARRAY.
 * * The function accepts following parameters:
 * *  1. INTEGER rideDuration
 * *  2. INTEGER_ARRAY songDurations
 * return best possible pair
 * <p>
 * We initially reduce the rideDuration by 30, as the sum of the songDurations needs to be rideDuration - 30.
 * <p>
 * We initialize a map with the indices and durations of the songs
 * We sort the map so that we have the songs with the highest durations followed by the least indices at the end.
 * The special corner case in which all the songs have the same duration is handled
 * We iterate through the map in a reversed fashion and each time
 * We check whether a pair is formed by looking up 'rideDuration - map.get(i)[0]' is in the map
 * In case the pair is formed, we insert it into 'ans'
 * The song index of the current song is mapped to its duration for later lookup
 * Handling the corner case of no possible pairs
 * Sort the ans vector to find out the best possible pair
 * Return the best possible pair
 * The complexity of code is O(n) space and O(n log n) time where n is the number of songs.
 * <p>
 * The log n factor comes in due to the look - up time in the hashtable and sorting the vectors v and ans each of size O(n)
 * https://github.com/deepika087/CompetitiveProgramming/blob/d40c24736a6fee43b56aa1c80150c5f14be4ff22/CompaniesHiringQuestions/Amazon%20OA%20%7C%20Amazon%20Music%20Runtime.py
 * https://github.com/TheDusKnight/coding/blob/86e53fb64d7da461fa80a906b6e7e4e8de25f0b3/mianjing/amazon_oa/AmazonMusicPair/Solution2.java
 * https://github.com/AbhJ/some-cp-files-3/blob/e579fa9bd4376337e203818b874f76b276c987ea/amazon-lux-coding-test-may-22-2022/amazon_q1.cpp
 * https://github.com/aditi1122000/Competetive-Programming/blob/7d144dd540cf8aa30463baf38cce361d6fb7667b/%23Amazon%20music%20feature%20for%20bus%20rides
 */
public class FindSong {
    public static void main(String[] args) {
        FindSong test = new FindSong();
        List<Integer> songDurations = Arrays.asList(5,55,30,30,30,40);
        int rideDuration = 120;
        System.out.println(test.findSongs(rideDuration, songDurations));
        System.out.println(IDsOfSongs(rideDuration, songDurations));

        songDurations = Arrays.asList(1, 2, 40, 30);
        rideDuration = 72;
        System.out.println(IDsOfSongs(rideDuration, songDurations));
        System.out.println(test.findSongs(rideDuration, songDurations));

    }

    // don't understand
    public List<Integer> findSongs(int rideDuration, List<Integer> songDurations) {
        Map<Integer, Integer> map = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < songDurations.size(); i++) {
            Integer checkKey = map.get(rideDuration - 30 - songDurations.get(i));
            if (checkKey != null)
                ans.add(Arrays.asList(checkKey, i));
            map.putIfAbsent(songDurations.get(i), i);
        }

        if (ans.size() == 1)
            return ans.get(0);
        if (ans.size() > 1) {
            int min = Integer.MAX_VALUE;
            int minIdx = -1;
            for (int i = 0; i < ans.size(); i++) {
                int localMin = Math.min(songDurations.get(ans.get(i).get(0)), songDurations.get(ans.get(i).get(1)));
                if (min > localMin) {
                    min = localMin;
                    minIdx = i;
                }
            }
            return ans.get(minIdx);
        }
        return Arrays.asList(-1, -1);
    }

    private static class Pair{
        int index;
        int duration;
        public Pair(int index, int duration) {
            this.index = index;
            this.duration = duration;
        }
    }

    public static List<Integer> IDsOfSongs(int rideDuration, List<Integer> songDurations) {
        List<Pair> list = new ArrayList<>();
        for (int i = 0; i < songDurations.size(); i++) {
            list.add(new Pair(i, songDurations.get(i))); // index, duration
        }
        list.sort(Comparator.comparingInt(a -> a.duration)); //按照duration从小到大排
        int left = 0;
        int right = songDurations.size() - 1;

        List<Integer> ans = new ArrayList<>();
        while (left < right) {
            int sum = list.get(left).duration + list.get(right).duration;
            if (sum == rideDuration - 30) {
                ans.add(left);
                ans.add(right);
                return ans;
            } else if (sum > rideDuration - 30) {
                right--;
            } else {
                left++;
            }
        }
        return Arrays.asList(-1, -1);
    }

}
