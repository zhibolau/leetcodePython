import java.util.Arrays;

public class MakePowerNonDecreasing {
    public static int MinimumPower(int []arr){
        int arrSize = arr.length;
        int dp[] = new int[arrSize];
        for (int i = 1; i < arrSize; i++) {
            dp[i] = dp[i-1]+Math.max(arr[i-1]-arr[i],0);
        }
        System.out.println(Arrays.toString(dp));
        return dp[arrSize-1];
    }

    public static int nonDecreasing(int []arr){
        int arrSize = arr.length;
        int ans = 0;
        if (arrSize == 1) return arr[0];
        for (int i = 1; i < arrSize; i++) {
            arr[i] += ans;
            if (arr[i] < arr[i - 1]) ans += arr[i - 1] - arr[i];
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(MinimumPower(new int[]{3, 4, 1, 9, 2}));
        System.out.println(nonDecreasing(new int[]{3, 4, 1, 9, 2}));
    }
}
