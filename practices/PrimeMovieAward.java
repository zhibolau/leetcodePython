import java.util.Arrays;

/**
 * awards 分组，每组max-min不超过k， 就直接sort一遍，然后贪心的把最大能加到当前组的加进来， 加不进来的count++, 换个 新组
 * Divide movies into groups based on the number of awards they have won.
 * A group can consist of any number of movies, but the difference in the number of awards won by any 2 movies in the group must not exist k.
 * determine the minimum number of groups that can be formed such that each movie is in exactly one group
 * <p>
 * i.e. [1,5,4,6,8,9,2], k=3
 * [1,2], [4,5,6], [8,9] => diff of any 2 movies is < 3 => return 3组
 */
public class PrimeMovieAward {
    public static void main(String[] args) {
        PrimeMovieAward test = new PrimeMovieAward();
        System.out.println(test.minGroup(new int[]{1, 5, 4, 6, 8, 9, 2}, 3));
    }

    public int minGroup(int[] movies, int k) {
        Arrays.sort(movies);
        int ans = 1;
        int min = movies[0];
        for (int i = 1; i < movies.length; i++) {
            if (movies[i] - min > k) {
                min = movies[i];
                ans++;
            }
        }
        return ans;
    }
}
